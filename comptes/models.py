from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.models import AbstractUser
from PIL import Image,ImageDraw
# Create your models here.
class MyUser(AbstractUser):
    USER_TYPE_CHOICES = (
           ('admin', 'Admin'),
           ('universite', 'Universite'),
           ('sec', 'Secretaire'),
       )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    USERNAME_FIELD='username'
    groups = models.ManyToManyField(Group, related_name='myuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='myuser_set', blank=True  )
    def has_perm(self,perms):
        return True
    def has_module_perms(self,app_label):
        return True 
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

class Institution(models.Model):
    user=models.OneToOneField(MyUser, on_delete=models.CASCADE)
    denom=models.CharField(max_length=100,null=True,blank=True)
    abreviation=models.CharField(max_length=100,null=True,blank=True)
    logos=models.ImageField(upload_to='logos',null=True)




