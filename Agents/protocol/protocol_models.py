from tortoise import fields, models
from typing import List
from uagents import Model

class summary(models.Model):
    text=fields.TextField()

class quiz(models.Model):
    questions=List[str]
    answers=List[str]

class QuizParams(Model):
    questions: str
    answers: str

class summaryRequest(Model):
    url: str

class summaryResponse(Model):
    summary: str

class quizRequest(Model):
    url: str
    numQuestions: int

class sendQuestions(Model):
    questions: List[str]
    answers: List[str]

class submitAnswers(Model):
    answers: List[str]

class results(Model):
    grade: str
    feedback: List[str]

class Empty(Model):
    pass