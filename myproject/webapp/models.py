from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser,BaseUserManager

# model for department
class Department(models.Model):
    id              = models.AutoField(primary_key=True)
    code            = models.CharField(max_length=200)
    description     = models.TextField()

    class Meta:
        ordering =["code"]
    
    def __str__(self):
        return self.code

# for creating super user only
class MyAccountManager(BaseUserManager):
    def create_superuser(self,username,email,password=None):
        dept= Department.objects.get(pk=1)
        user = self.model(username=username,
                                email=email,
                                department = dept,
                                is_admin=True,
                                is_staff=True,
                                is_superuser=True)
        user.set_password(password),
        user.save(using=self._db)
        return user

class User(AbstractUser):
    id              = models.AutoField(primary_key=True)
    username        = models.CharField(max_length=200,unique=True)
    password        = models.CharField(max_length=100)
    email           = models.EmailField(max_length=200,unique=True)
    department      = models.ForeignKey(Department,on_delete=models.CASCADE)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    objects=MyAccountManager()

    #required fields
    USERNAME_FIELD ='username'
    REQUIRED_FIELDS =['email','password']

    

    class Meta:
        ordering =["username"]
    
    def __str__(self):
        return self.username

    #if user has admin permission
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    #if user has module permission
    def has_module_perms(self, app_label):
        return True


  


