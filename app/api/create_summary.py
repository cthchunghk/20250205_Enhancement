from flask_restful import Resource
from flask import current_app
from flask import request
import re
from app.openai.text_generating import SummaryGenerator
from app.api.json_factory import JSONFactory


class CreateSummary(Resource):

    def post(self):
        data = request.get_json()
        text = data['text']
        sg = SummaryGenerator()
        summary = sg.createSummary(text)
        result_array = summary.split('\n')
        title = re.sub(r'.*: *', '', result_array[0]).strip()
        content = re.sub(r'.*: *', '', result_array[1]).strip()
        paylaod = [{
            'title': title,
            'summary': content
        }]
        return JSONFactory().createResponse(True, paylaod)
