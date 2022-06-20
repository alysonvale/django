from datetime import datetime
from ninja import Schema

class TrackSchema(Schema):
    id: str
    question: str
    choice: str

class NotFoundSchema(Schema):
    message: str