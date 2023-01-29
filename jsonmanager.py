from json import load, dump
from json.decoder import JSONDecodeError
from hashlib import sha256


class JsonManager:
    def __init__(self) -> None:
        self.__FILE: str = 'data.json'    

    def load_file(self) -> dict:
        try:
            with open(self.__FILE, encoding='utf-8') as f:
                obj_json: dict = load(f)
        except (FileNotFoundError, JSONDecodeError):
            with open(self.__FILE, 'w+',encoding='utf-8') as file_error_json:
                SHOW_ERROR: dict = {'message': 'error'}
                dump(SHOW_ERROR, file_error_json, indent=4)

        with open(self.__FILE, encoding='utf-8') as file_json:
            obj_json = load(file_json)
        return obj_json

    def insert(self, data: dict) -> None:
        ENCODED: tuple[bytes] = (f"{data['user']}".encode('utf-8'),
                                 f"{data['email']}".encode('utf-8'),
                                 f"{data['pass']}".encode('utf-8'))
        
        data['user'] = sha256(ENCODED[0]).hexdigest()
        data['email'] = sha256(ENCODED[1]).hexdigest()
        data['pass'] = sha256(ENCODED[2]).hexdigest()

        with open(self.__FILE, 'w+', encoding='utf-8') as f:
           dump(data, f, indent=4)
