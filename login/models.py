from django.db import models

# Create your models here.
class SignIn (models.Model):
    iduser = models.AutoField(db_column='iduser', primary_key='true')
    fullname = models.CharField(db_column="fullname", blank=True, null= True, max_length=50)
    city = models.CharField(db_column="city", blank=True, null= True, max_length=50 )
    age = models.CharField(db_column="age", blank=True, null= True, max_length=50)
    email  = models.CharField(db_column='email',blank=True, null= True, max_length=50)
    password = models.CharField(db_column='password',blank=True, null= True, max_length=8)
    class Meta :
        managed = False
        db_table = 'SignIn'