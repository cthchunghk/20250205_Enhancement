import os
from dotenv import load_dotenv

from openai import OpenAI



class Config():

    load_dotenv()
    apiKey = os.getenv('APIKEY')
    client = OpenAI(api_key=apiKey)

    


    # @property
    # def apiKey(self):
    #     return self._apiKey
    
    # @apiKey.setter
    # def apiKey(self, v):
    #     self._apiKey = v

    # def getAPIKey(self):
    #     return self.apiKey
    
