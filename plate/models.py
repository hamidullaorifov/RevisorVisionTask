from django.db import models
import uuid
# Create your models here.

class Plate(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    number = models.CharField(max_length=50)
    
