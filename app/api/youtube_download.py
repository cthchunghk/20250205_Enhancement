from flask_restful import Resource
from flask import current_app
from flask import request

from app.api.json_factory import JSONFactory
from app.utils.youtube_downloader import YouTubeDownloader

class ClipDownloader(Resource):

    def post(self):
        data = request.get_json()
        url = data['url']
        current_app.logger.info(url)
        storedPath = YouTubeDownloader.downloadAudio(url)       
        paylaod = [{            
            'store_path': storedPath
        }]
        return JSONFactory().createResponse(True, paylaod)