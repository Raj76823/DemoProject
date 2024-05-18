from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):



    USERNAME_FIELD ='username'
    phone= models.CharField(unique=True, max_length=50,null=True,blank=True)


    def __str__(self) -> str:
        return super().username
    

    def get_fullname(self):
        return(
            self.username
            if not self.first_name and not self.last_name
            else f"{self.first_name} {self.last_name}"
        )
    
    def delete(self,*args, **kwargs):
        if self.is_staff:
            self.is_staff=False
            self.save()


    class Meta:
         managed = settings.MANAGE_DATABASE
         db_table = "User"
         verbose_name_plural = "Users"
    
         if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
         