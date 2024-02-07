from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _colection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)
