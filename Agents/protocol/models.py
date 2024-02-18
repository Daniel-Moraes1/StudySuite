from tortoise import fields, models
from typing import List

class summary(models.Model):
    text=fields.TextField()

class quiz(models.Model):
    questions=List[str]
    answers=List[str]

class empty(models.Model):
    pass