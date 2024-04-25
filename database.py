import os
import json
import secrets

# from Crypto.Cipher import AES
from cryptography.fernet import Fernet


key = b"66ZVNbmptsArAK8vYV07evCi9Tt6wIiNPugme-7D15M="


class Database:
    def __init__(self, directory: str) -> None:
        self.directory = directory

    def __encrypt(self, data: str):
        return Fernet(key).encrypt(data.encode()).decode()

    def __decrypt(self, data: str):
        return Fernet(key).decrypt(data.encode()).decode()

    def _read(self, shorted: str):
        with open(self.directory + "/" + "/data.json", "r") as f:
            data = json.loads(f.read())

        return self.__decrypt(data.get(shorted))

    def _write(self, url: str):
        with open(self.directory + "/" + "data.json", "r") as f:
            data = json.loads(f.read())

        with open(self.directory + "/" + "data.json", "w") as f2:
            shorted = secrets.token_hex(48)
            data[shorted] = self.__encrypt(url)
            f2.write(json.dumps(data, indent=5))

        return shorted

    def get_url(self, data: str):
        return self._read(data)

    def add_url(self, url: str):
        return self._write(url)
