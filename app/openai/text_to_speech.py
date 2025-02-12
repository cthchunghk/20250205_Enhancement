from pathlib import Path
import os
import base64
from datetime import datetime


from app.openai.config import Config as c
from app.utils.path_setting import speech_file_path as s



class TextToSpeech():
    
    #client = OpenAI(api_key=c.apiKey)
    
   
    #speech_file_path = f'{os.path.dirname(os.path.abspath(__file__))}/asset/downloads/speech.mp3'
    create_time =  datetime.now()
    formatted_date = create_time.strftime("%Y%m%d-%H%M%S")
    output_format = 'mp3'
    speech_file_path = f'{os.path.join(s, formatted_date+'.'+output_format)}'
    def createResponse(self, content: str) -> str:
        #print(f'API Key = {self.client.api_key}')
        #print(f'{self.speech_file_path}')
        formatted_content = f"""
        你需要使用純正廣東話朗讀以下內容必須根據以下規則。
        1. 口語化朗讀：用純正廣東話口語風格朗讀。如果文本是書面語，需將其轉化為純正廣東話口語。外語部分則直接讀出，不需轉化。
        3. 專注內容：只讀指定講稿內容，不添加額外資訊。
        5. 專有名詞：專有名詞發音需清晰，確保不遺漏或誤讀。
        6. 數字處理：朗讀數字時需慢慢讀，避免將「十、百、千、萬」弄錯。
        9. 數字轉換：若文本中有數字，不需要理會數字中的,或逗號，然後需轉為中文數字格式。例如：
        「100」→「一百」
        「1000」→「一千」
        「10000」→「一萬」
        「100000」→「十萬」
        「1000000」→「百萬」
        10. 日期轉換：若文本中有日期，需轉為中文日期格式。例如：
        「2022-01-01」→「二零二二年一月一日」
        11. 時間轉換：若文本中有時間，需轉為中文時間格式。例如：
        「13:00」→「下午一時」
        12. 貨幣轉換：若文本中有貨幣，需轉為中文貨幣格式。例如：
        「$100」→「一百港元」
        13. 百分比轉換：若文本中有百分比，需轉為中文百分比格式。例如：
        「50%」→「百分之五十」
        14. 電話號碼轉換：若文本中有電話號碼，需轉為中文電話格式。例如：
        「123-4567」→「一二三四五六七」
        15. 電郵號碼轉換：若文本中有電郵地址，需要每個字母單獨讀出。例如：
        「info@2cexam.com」→「i n f o @ 2 c e x a m . c o m」

        以下是我需要你朗讀的文本
        [{content}]"""

        # Create completion with both text and audio using OpenAI's API
        # print(f"Generating audio for {txt_file}...")
        completion = c.client.chat.completions.create(
            model="gpt-4o-mini-audio-preview",     # Specify the model to use
            modalities=["text", "audio"],      # Request both text and audio output
            audio={"voice": "ballad",          # Specify voice type
                "format": self.output_format},           # Specify output format
            messages=[
                {
                    "role": "user",
                    "content": formatted_content
                }
            ]
        )
        print('Response Received')
        # Decode the base64-encoded audio response and save to file
        response_bytes = completion.choices[0].message.audio.data
        mp3_bytes = base64.b64decode(response_bytes)
        with open(self.speech_file_path, "wb") as f:
            f.write(mp3_bytes)
        print('File Saved')
        print(f"Successfully generated")
        return response_bytes, self.speech_file_path
    
