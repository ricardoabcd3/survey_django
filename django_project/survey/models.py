from django.db import models
from django.utils import timezone
import datetime
# models
class Question(models.Model):
    question_text= models.CharField(max_length=2000)
    pub_date=models.DateField("date publish")
    def __str__(self):
        return self.question_text+' at '+str(self.pub_date)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    #on delete models cascade = delete all thins releted to Question so important
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choise_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choise_text

