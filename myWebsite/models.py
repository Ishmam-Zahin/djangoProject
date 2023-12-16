from django.db import models

class MyTable(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    time = models.DateField(null=True)

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    publish_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
# Create your models here.