from json import load, dump
from json.decoder import JSONDecodeError


class JsonManager:
    def __init__(self) -> None:
        self.__FILE: str = 'data.json'    

    def load_file(self):
        try:
            with open(self.__FILE, encoding='utf-8') as f:
                obj_json = load(f)
        except (FileNotFoundError, JSONDecodeError):
            with open(self.__FILE, 'w+',encoding='utf-8') as file_error_json:
                SHOW_ERROR: dict = {'message': 'error'}
                dump(SHOW_ERROR, file_error_json, indent=4)

        with open(self.__FILE, encoding='utf-8') as file_json:
            obj_json = load(file_json)
        return obj_json

    def insert(self, data: dict) -> None:
        with open(self.__FILE, 'w+', encoding='utf-8') as f:
            dump(data, f, indent=4)
