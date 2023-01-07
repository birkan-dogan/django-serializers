from django.db import models

# Create your models here.

class Path(models.Model):
    path_name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.path_name}"

class Student(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 50)
    number = models.IntegerField()
    age = models.IntegerField(default = 25)
    path = models.ForeignKey(Path, related_name = "students", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.number}-{self.last_name} {self.first_name}"