from django.db import models

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Property(BaseModel):
    status = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    fetched_from = models.CharField(max_length=200)
    propertyId = models.CharField(max_length=10, default="")
    class Meta:
        verbose_name_plural = "Properties"
