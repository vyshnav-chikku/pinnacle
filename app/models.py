from django.db import models

# Create your models here.

class employee_tb(models.Model):
    fname = models.CharField(max_length=200,null='empty')
    lname = models.CharField(max_length=200,null='empty') #removed
    email = models.CharField(max_length=200,null='empty')
    phone = models.CharField(max_length=200,null='empty')
    dob = models.CharField(max_length=200,null='empty') 
    age = models.CharField(max_length=200,null='empty') #auto calculate
    gender = models.CharField(max_length=200,null='empty') #removed
    marital_status = models.CharField(max_length=200,null='empty') #removed
    address = models.TextField(null='empty') #removed
    language = models.TextField(null='empty') #removed
    qalification = models.TextField(null='empty')
    experience = models.TextField(null='empty') #inyear
    jobopted = models.TextField(null='empty') #linkedin
    compknowledge = models.TextField(null='empty') #removed
    resume = models.FileField(upload_to='employe_resume',null='empty')
    date = models.CharField(max_length=200,null='empty')




class employer_tb(models.Model):
    logo = models.ImageField(upload_to='employer_logo',null='empty')
    nameorg = models.TextField(null='empty')
    rname = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    phone = models.CharField(max_length=200,null='empty')
    phoner = models.CharField(max_length=200,null='empty')
    designation = models.TextField(null='empty')
    address = models.TextField(null='empty')
    website = models.URLField(max_length=500,null='empty')
    
    job_file = models.FileField(upload_to='employer_file',null='empty')    
    date = models.CharField(max_length=200,null='empty')

  
    

class admin_tb(models.Model):
    name = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    password = models.TextField(null='empty')
    pwd = models.TextField(null='empty')
    date = models.CharField(max_length=200,null='empty')
    



class employee_tb_jobfair(models.Model):
    name = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    phone = models.CharField(max_length=200,null='empty')
    qualification = models.TextField(null='empty')
    experience = models.CharField(max_length=200,null='empty')
    linkedin = models.TextField(null='empty')
    category = models.TextField(null='empty')
    resume = models.FileField(upload_to='employe_resume',null='empty')
    date = models.CharField(max_length=200,null='empty')





class employer_tb_jobfair(models.Model):
    nameorg = models.TextField(null='empty')
    rname = models.CharField(max_length=200,null='empty')
    email = models.CharField(max_length=200,null='empty')
    phone = models.CharField(max_length=200,null='empty')
    designation = models.TextField(null='empty')
    address = models.TextField(null='empty')
    website = models.URLField(max_length=500,null='empty')   
    job_file = models.FileField(upload_to='employer_file',null='empty')    
    date = models.CharField(max_length=200,null='empty')
