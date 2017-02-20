from django.db import models
# Create your models here.

class Clipboard(models.Model):
    paste_text = models.CharField(max_length=3000)
    create_date = models.DateTimeField('create date')