from django.db import models

# Create your models here.


class topics(models.Model):
    topics_name=models.CharField(max_length=100,primary_key=True)
class webpage(models.Model):
    topics_name=models.ForeignKey(topics,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
class accessrecords(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    data=models.DateField()
    author=models.CharField(max_length=100)