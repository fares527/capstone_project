from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    describtion = models.TextField()
    dwg_file = models.FileField(upload_to='dwg_files/')
    pdf_file = models.FileField(upload_to='pdf_files/')
    updated_date = models.DateTimeField()
    tags = models.CharField(max_length=250)