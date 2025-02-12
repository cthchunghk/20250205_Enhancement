from flask_restful import Resource
from flask import current_app
import json
from flask import request
import os

# Test only
class Test(Resource):

    def __init__(self):
        pass
        #self.storage_service = storage_service.StorageService(os.environ.get('s3_bucket'))

    
    def get(self, id):
        # x = self.storage_service.get_file('text')
        # text = json.loads(x["Body"].read().decode())
        # print(text['payloads'])       
        #return self.storage_service.list_file()
        #return os.environ.get('ai_model_labels').split(";")
        #return [current_app.config.get("API_KEY")]
        #current_app.config.keysprint(``)
        #print(current_app.config)        
        #return DetectionClass().getLabelNames()
       # return current_app.send_static_file('/static/road_cam.png')
        print('on9')
        current_app.logger.info(id)
        return id

    def post(self):
        data = request.get_json()
        current_app.logger.info(data['data'])
        #self.storage_service.upload_file(bytes(json.dumps(data['data']).encode('UTF-8')), 'test')
        return True