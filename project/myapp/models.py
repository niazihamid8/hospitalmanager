from django.db import models

# Create your models here.
class member(models.Model):
    emil= models.EmailField(max_length=100)
    pw= models.CharField(max_length=12)
    ln= models.CharField(max_length=12)
    ac= models.CharField(max_length=12)
    fn= models.CharField(max_length=12)
    en= models.CharField(max_length=12)
    la= models.CharField(max_length=12)



class vahed(models.Model):
    pelak= models.CharField(max_length=100)
    metraj= models.CharField(max_length=100)
    telephon= models.CharField(max_length=100)
    parking= models.CharField(max_length=100)



class personnel(models.Model):
    semat= models.CharField(max_length=100)
    mellicode= models.CharField(max_length=100)
    personnelcode= models.CharField(max_length=100)
    pass1= models.CharField(max_length=100)
    mobile= models.CharField(max_length=100)
    telephon= models.CharField(max_length=100)
    fn= models.CharField(max_length=100)
    ln= models.CharField(max_length=100)
    enddate= models.DateField(max_length=100)
    startdate= models.DateField(max_length=100)

    personneltype= models.CharField(max_length=100)
    admin= models.CharField(max_length=100)

class shift(models.Model):
    id = models.AutoField(primary_key=True)
    fn= models.CharField(max_length=100)
    ln= models.CharField(max_length=100)
    post= models.CharField(max_length=100)
    bakhsh= models.CharField(max_length=100)
    enddate= models.DateTimeField(max_length=100)
    startdate= models.DateTimeField(max_length=100)

class morakhasi(models.Model):
    id = models.AutoField(primary_key=True)
    personnelcode= models.CharField(max_length=100)
    fn= models.CharField(max_length=100)
    ln= models.CharField(max_length=100)
    post= models.CharField(max_length=100)
    bakhsh= models.CharField(max_length=100)
    enddate= models.DateTimeField(max_length=100)
    startdate= models.DateTimeField(max_length=100)
    comment= models.TextField(max_length=1000)
    adminaccept=models.CharField(max_length=100)


class user(models.Model):
    fn=models.CharField(max_length=50)
    ln=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    un=models.CharField(max_length=30)
    pw=models.CharField(max_length=50)

class userh(models.Model):
    fn=models.CharField(max_length=50)
    ln=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    un=models.CharField(max_length=30)
    pw=models.CharField(max_length=50)
    num=models.CharField(max_length=50)
    admin=models.CharField(max_length=50)
