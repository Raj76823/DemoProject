from django.db import models

# Create your models here.
from Abstract.managers import BaseManager

from django.conf import settings

class BaseModel(models.Model):
    operating_user=None
    objects=BaseManager()
    status= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)


    """
    created_by = models.ForeignKey("User.User",related_name="%(class)s_created_by", on_delete=models.DO_NOTHING,blank=True)
    updated_by=models.ForeignKey("User.User",related_name="%(class)s_updated_by",on_delete=models.DO_NOTHING,blank=True)
    
    def save(self,*args, **kwargs):

        operating_user= (
            self.operating_user if hasattr(self,"operating_user") else None
        )
        self.updated_by = operating_user
        if not self.pk:
            self.created_by=operating_user
            super().save(*args, **kwargs)
    """
    def delete(self,*args, **kwargs):
        self.status=False
        self.save(*args, **kwargs)

    class Meta:
        abstract=True
        ordering=["-update_at"]
        if not settings.DEFAULT_PERMISSIONS:
            default_permissions = []
           