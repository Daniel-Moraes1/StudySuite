from typing import List
from uagents import Context, Model, Protocol

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


summary_proto = Protocol(name="summmary", version="0.1.0")
quiz_proto = Protocol(name="quiz", version="0.1.0")