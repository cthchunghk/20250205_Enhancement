from flask_restful import Resource
from flask import current_app
from flask import request
from app.api.json_factory import JSONFactory

import app.utils.web_scarping as ws


class Scrape(Resource):

    def post(self):
        data = request.get_json()
        url = data['url']
        page_detail = ws.scrapeContent(url)
        paylaod = [{
            'page_detail': page_detail
        }]
        return JSONFactory().createResponse(True, paylaod)
