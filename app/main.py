import os

from logging.config import dictConfig

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import app.utils.path_setting as ps
from app.api.test import Test
from app.api.create_summary import CreateSummary
from app.api.create_text_response import CreateTextResponse
from app.api.youtube_download import ClipDownloader
from app.api.transcript import Transcript
from app.api.text_to_speech import TextToSpeech
from app.api.scrape import Scrape
from app.api.scrape_all import ScrapeAll
import app.api as a

api_base = '/api/'

# Create Flask
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Set environment 
#app.config.from_pyfile('settings.py')

# Make RESTful API
rest_api = Api(app)

# Add CORS Support
CORS(app)

# Follow the sequence on how your shit is implement in the class
rest_api.add_resource(Test, f'{api_base}test/<id>', f'{api_base}test')
rest_api.add_resource(CreateSummary, f'{api_base}/summary')
rest_api.add_resource(CreateTextResponse, f'{api_base}/response/text')
rest_api.add_resource(ClipDownloader, f'{api_base}/download/clip')
rest_api.add_resource(Transcript, f'{api_base}/transcript')
rest_api.add_resource(TextToSpeech, f'{api_base}/response/speech')
rest_api.add_resource(Scrape, f'{api_base}/scrape/page')
rest_api.add_resource(ScrapeAll, f'{api_base}/scrape/all')


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

os.makedirs(ps.system_reserved_path, exist_ok=True)
os.makedirs(ps.youtube_download_path, exist_ok=True)
os.makedirs(ps.speech_file_path, exist_ok=True)

app.logger.info("OK")
if __name__ == "__main__":
    ## Only if you want to run in Prod:
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run()




    