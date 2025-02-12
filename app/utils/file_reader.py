import json


class DataReader():
    def read(self, path: str):
        pass


class LocalJSONFileReader(DataReader):

    def read(self, path: str) -> list:
        # Open and read the JSON file
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data
