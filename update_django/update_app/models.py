from django.db import models

# Create your models here.
class update_db(models.Model):
    Name=models.CharField(max_length=25,null=True,blank=True)
    Date=models.DateField(max_length=20,null=True,blank=True)
    Workfh=models.CharField(max_length=5,null=True,blank=True)
    Updates=models.CharField(max_length=200,null=True,blank=True)
    Comments=models.CharField(max_length=200,null=True,blank=True)
    Images=models.ImageField(upload_to="profile",null=True,blank=True)