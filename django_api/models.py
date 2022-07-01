import email
from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    def __str__(self):
         if self.name==None:
           return "ERROR-CUSTOMER NAME IS NULL"
         else:
            return self.name
         
class Meta:
    db_table="user" 


      
   
       



 


