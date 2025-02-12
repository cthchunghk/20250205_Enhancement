# import sys
import os
from pathlib import Path
# sys.path.append(os.path.abspath(os.path.join(os.path.join(__file__, os.pardir),os.pardir)))

from app.utils.youtube_downloader import YouTubeDownloader as yd
import app.openai.config as c
from app.openai.text_to_speech import TextToSpeech as tts
from app.openai.speech_to_text import SpeechToText as stt
from app.openai.text_generating import ResponseGenerator as tg
from app.utils.file_reader import LocalJSONFileReader
import app.utils.web_scarping as ws
from app.openai.text_generating import SummaryGenerator as sg
# import ..util.youtube_downloader as yd

# file_path = f'{os.path.join(Path("__file__").absolute().parent, 'asset', 'downloads', 'speech.mp3')}
file_path = f'{os.path.join(Path("__file__").absolute().parent, 'asset', 'data', 'faqs.json')}'

if __name__ == '__main__':    
   # print(tg().createResponseFromFAQ("國際運送有沒有額外費用"))
    # d = LocalJSONFileReader().read(file_path)
    # q = []
    # a = []
    # for i in d:
    #     q.append(i['question'])
    #     a.append(i['answer'])
    
    # #print(f'{q}')

    # result = "\n".join(
    # [f"{i + 1}. Q: {q} A: {a[i]}" for i, q in enumerate(q)])
    #print(result)
    #config = c.Config()
    #print(config.apiKey)
    #tts()
    #stt().transcription(f'{os.path.join(Path("__file__").absolute().parent, 'asset', 'downloads', 'speech.mp3')}')
    #.createResponse("E3 展主辦單位展開新活動「iicon 開發互動創新大會」，但跟玩家沒啥關聯")
    #download_path = yd.downloadAudio('https://www.youtube.com/watch?v=7CLYU-WQ-Wk')
    #scripts = stt().transcription(download_path)
    #print(scripts)
    #print('HI')

    #a = ws.scrape('https://www.buyandship.today/')
 #  for i in range(len(a)):
   #    #r = sg().createSummary(d)
   #    #if i > 5:
   #       #break
   #    knowledge = f'Title: {a[i]['title']} Content: {a[i]['content']}'
   #    r = sg().createSummary(knowledge)
   #    print(r)
   #    #print(f'Title: {a[i]['title']} Content: {a[i]['content']}')
   #    print(' === ')
   #  for d in a:
   #      print(d['content'])

    d = ws.scrapeContent('https://www.buyandship.today/restrictions/')
   #knowledge = f'Title: {d['title']} Content: {d['content']}'
    knowledge = f'Content: {d['content']}'
    print(d)
   # r = sg().createSummary(knowledge) 
   # print(r)


