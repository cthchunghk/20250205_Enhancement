from flask_restful import Resource
from flask import current_app
from flask import request
from app.api.json_factory import JSONFactory

from app.openai.text_to_speech import TextToSpeech as tts

class TextToSpeech(Resource):
        
    def post(self):
        data = request.get_json()
        text = data['text']        
        byte, file_path = tts().createResponse(text)
        paylaod = [{
            'file_path': file_path
        }]
        return JSONFactory().createResponse(True, paylaod)