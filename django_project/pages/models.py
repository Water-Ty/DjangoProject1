from django.db import models

# Create your models here.


class TestModel(models.Model):
    name=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
