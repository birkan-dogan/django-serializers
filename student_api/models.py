from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 50)
    number = models.IntegerField()
    age = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.first_name