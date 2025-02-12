from flask_restful import Resource
from flask import current_app
from flask import request
from app.api.json_factory import JSONFactory

from app.openai.text_generating import ResponseGenerator


class CreateTextResponse(Resource):

    def post(self):
        data = request.get_json()
        question = data['question']
        rg = ResponseGenerator()
        response = rg.createResponseFromFAQ(question)
        response = response.replace('A: ', '')
        paylaod = [{
            'question': question,
            'response': response
        }]
        return JSONFactory().createResponse(True, paylaod)