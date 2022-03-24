from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Editor(models.Model):
    body=RichTextField(blank=True, null=True)

class Debug(models.Model):
    debug=models.CharField(max_length=10)