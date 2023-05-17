from django.db import models

# Create your models here.


class Employee(models.Model):
    ename=models.CharField(max_length=50)
    eid=models.IntegerField()
    job=models.CharField(max_length=20)
    sal=models.IntegerField()