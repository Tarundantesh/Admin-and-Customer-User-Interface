from django.db import models

# Create your models here.
class AccountHolder(models.Model):
    Name=models.CharField(max_length=10)
    Aadhar=models.IntegerField()
    PAN=models.CharField(max_length=20)
    Contact=models.IntegerField()
    Balance=models.FloatField()
    Account_Type=models.CharField(max_length=15)
