from django.db import models

class ComplaintReg(models.Model):
    name =models.CharField(30)
    phone =models.IntegerField()
    complaint =models.TextField(100)
