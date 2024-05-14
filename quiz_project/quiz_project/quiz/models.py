from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    correct_option = models.PositiveSmallIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')])
    
    def __str__(self):
       return self.question_text
    
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.PositiveBigIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')])

    def is_correct(self):
        return self.selected_option == self.question.correct_option

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usr_name = models.CharField(max_length=255)  # usr_nameに関連づけられたUserのユーザー名を格納するためのCharField
    score = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Scoreインスタンスを保存する際にusr_nameを設定する
        self.usr_name = self.user.username
        super().save(*args, **kwargs)
