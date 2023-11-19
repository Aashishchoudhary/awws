from rest_framework import serializers
from .models import *

class ImageSer(serializers.ModelSerializer):
    class Meta:
        model=ImageFi
        fields='__all__'