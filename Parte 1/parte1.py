# Codigo Parte 1

#### MODELS ####
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Adicionados metodos __str__

'''
À classe Question
def __str__(self):              # __unicode__ on Python 2
        return self.question_text
		
À classe Choice
def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
		
'''

# Adicionado metodo was_published_recently na classe Question

'''
import datetime
from django.utils import timezone

def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

'''