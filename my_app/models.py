from django.db import models

from django.db import models

class Ping(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    

class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_mobile = models.CharField(max_length=10)
    stu_city = models.CharField(max_length=15)
    
    def __str__(self):
        return self.stu_name