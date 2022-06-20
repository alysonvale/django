from dataclasses import field
from datetime import datetime
from ninja import Schema, ModelSchema
from ninja.orm import create_schema
from tracks.models import Track


TrackSchema = create_schema(Track, fields=['title', 'last_play', 'artist', 'duration'])

# O de cima é a mesma coisa  do de baixo 

""" class TrackSchema(ModelSchema):
    class Config:
        model = Track
        model_fields = ['title', 'last_play', 'artist', 'duration'] """



class NotFoundSchema(Schema):
    messege: str