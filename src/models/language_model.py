from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    def to_dict(self):
        return {"name": self.data["name"], "acronym": self.data["acronym"]}

    @classmethod
    def list_dicts(cls):
        data = cls.find()
        for language in data:
            return language.to_dict()
