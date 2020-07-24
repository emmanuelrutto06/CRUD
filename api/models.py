from django.db import models
from datetime import datetime, date

class students(models.Model):
    firstname=models.CharField(max_length=24)
    lastname=models.CharField(max_length=24)
    student_id=models.IntegerField()
    stream=models.CharField(max_length=10, null=False)
    # Date_of_suspension=models.DateField(auto_now_add=False, auto_now=False, null=False)
    return_date=models.DateField(auto_now_add=False, auto_now=False, null=False)
    timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=False)
    Reason_of_suspension=models.CharField(max_length=2000, null=False)
    Teachers_sign=models.CharField(max_length=120, null=False)
    Adm_No = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.firstname
