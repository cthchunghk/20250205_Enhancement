from app.openai.config import Config as c
from app.utils.path_setting import embedding_path as ep
from app.utils.path_setting import faq_json_path as fp
from app.utils.file_reader import LocalJSONFileReader
import json
import numpy as np
from numpy.linalg import norm

class EmbeddingUtility():

    def createEmbedding(self, texts: list):
        questionList = []
        for t in texts:
            questionList.append(t['question'])
        self.saveEmbedding(questionList)

    def getEmbedding(self, text: str) -> list:
        response = c.client.embeddings.create(
            model="text-embedding-ada-002",
            input=text,
            encoding_format="float",
        )
        embeddings = response.data
        return embeddings
    
    def saveEmbedding(self, texts: list):
        embedding = []
        for t in texts:
            e = self.getEmbedding(t)
            embedding.append(e)
        with open(ep, "w") as outfile:
            json.dump(embedding, outfile)

    def loadEmbedding(self) -> list:
        with open(ep, 'r') as file:
            data = json.load(file)
        return data
    
    def getMostSimilarText(self, text: str):
        faqs = LocalJSONFileReader().read(fp)
        embeddings = self.loadEmbedding()
        text_embedding = self.getEmbedding(text)
        highestSimilarity = '-1'
        similarText = ''

        for i in range(len(embeddings)):
            cosine = np.dot(text_embedding, embeddings[i])/(norm(text_embedding)*norm(embeddings[i]))
            if cosine > highestSimilarity:
                highestSimilarity = cosine
                similarText = faqs[i]
        return similarText
