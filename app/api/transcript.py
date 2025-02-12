from flask_restful import Resource
from flask import current_app
from flask import request
from app.api.json_factory import JSONFactory

from app.openai.speech_to_text import SpeechToText

class Transcript(Resource):

    def post(self):
        data = request.get_json()
        file_path = data['file_path']
        stt = SpeechToText()
        script = stt.transcription(file_path)
        paylaod = [{
            'script': script
        }]
        return JSONFactory().createResponse(True, paylaod)