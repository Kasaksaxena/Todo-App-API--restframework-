from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

   class Meta:
       model=Todo #tell which model to serialize
       fields='__all__'# include all fields from model
       read_only_fields=['uuid','created_at','updated_at'] # Auto managed fields