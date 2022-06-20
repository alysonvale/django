from ninja import NinjaAPI
from .models import Choice, Question
from django.shortcuts import get_object_or_404
import json



api = NinjaAPI()

@api.get('question/')
def listar(request):
    question = Question.objects.all().values()

    return list(question)


@api.get('question/{id}')
def listar_question(request, id):
    question = get_object_or_404(Question, id=id)



