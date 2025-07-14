from ninja import Schema, ModelSchema
from . import models

class BookSchema(Schema):
    title: str
    author: str