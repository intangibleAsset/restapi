from django.db import models

# Create your models here.
class Employees(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    emp_id=models.IntegerField(unique=True)

    def __str__(self):
        return self.lastName
