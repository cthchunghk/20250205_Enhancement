import os
from pathlib import Path

from app.openai.config import Config as c
from app.utils.file_reader import LocalJSONFileReader
from app.utils.path_setting import faq_json_path
from app.openai.embedding import EmbeddingUtility


class ResponseGenerator():

    def __init__(self):
        self.json_path = faq_json_path

    def createResponseFromFAQ(self, query: str):
        systemMessage = self.createSystemMessage(
            LocalJSONFileReader().read(self.json_path))
        return self.__createResponse(query, systemMessage)

    def createResponseByVector(self, query: str):
        eu = EmbeddingUtility()
        simTextPair = eu.getMostSimilarText(query)
        systemMessage = self.createSystemMessage(simTextPair)
        return self.__createResponse(query, systemMessage)

    def __createResponse(self, query: str, systemMessage: str):
        userMessage = f'Q: {query}'
        completion = c.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {'role': "system", 'content': systemMessage},
                {'role': "user", 'content': userMessage},
            ],
            store=True
        )
        response = completion.choices[0].message.content.strip()
        return response

    def createSystemMessage(self, data: list) -> str:
        questionList = []
        answerList = []
        for i in data:
            questionList.append(i['question'])
            answerList.append(i['answer'])

        systemMessage = f'你是一個物流公司的客戶服務助理，這裡有一些問題和自訂答案：\n\n\
            {"\n".join(
            [f"Q: {q} A: {answerList[i]}" for i, q in enumerate(questionList)])}\n\n\
            請基於這些信息改進答案。\
            如果在這些信息中找不到資訊，請回答\"不好意思，我沒有相關資訊，請問您要跟我們的客戶服務助理對話嗎？\"'

        return systemMessage


class SummaryGenerator():
    prompt = 'Please base on the following text to create summary. \
        You should summarize it as "Title: The title of an element \nContent: The content of an element"\
        Summarize based on the title and business only. However, it should be as details as you can. \
        If you cannot find suitable content to summarize, please return: "Nothing useful" in the language used in text. \
        If there is no title provided, please summarize it from content. \
        Keep the language used in the text for your output.'

    def createSummary(self, text: str):
        userMessage = f'{text}'
        completion = c.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {'role': "user", 'content': f'{self.prompt}\n{userMessage}'},
            ],
            store=True
        )
        response = completion.choices[0].message.content.strip()
        return response


