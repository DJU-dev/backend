from django.conf import settings
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='dslr/post/%Y/%m/%d')
    caption = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
