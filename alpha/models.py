from django.db import models

# Create your models here.
def upload_path(instance,filname):
    return '/'.join(['covers',filname])
class ImageFi(models.Model):
    img=models.ImageField(upload_to=upload_path)
    name=models.CharField(max_length=30)