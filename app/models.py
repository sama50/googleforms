from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class UserForms(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=150)
    form_id = models.CharField(max_length=255)

    def __str__(self):
        return self.form_name
    
    

class SubmissionForm(models.Model):
    formid = models.ForeignKey(to=UserForms, on_delete=models.CASCADE)
    quetion = models.TextField()
    def __str__(self):
        return self.quetion

class QueationForImage(models.Model):
    formid = models.ForeignKey(to=UserForms, on_delete=models.CASCADE)
    quetion = models.TextField()
    def __str__(self):
        return self.quetion
     

class Queation_Text_ans(models.Model):
    email = models.EmailField(max_length=255)
    form_id = models.ForeignKey(to=UserForms, on_delete=models.CASCADE)
    que = models.ForeignKey(to=SubmissionForm, on_delete=models.CASCADE)
    ans = models.TextField()
    def __str__(self):
        return self.email


