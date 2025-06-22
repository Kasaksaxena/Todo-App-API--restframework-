from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField( auto_now_add=True)
    
    class Meta:
        abstract=True  #django doesnt create table for base model
    
class Todo(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    todo_title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)