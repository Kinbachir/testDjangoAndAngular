from django.db import models

class Document(models.Model):
    document = document = models.TextField(default="", blank=False, null=False)

class Annotation(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    label = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    document = models.ForeignKey(Document, related_name='annotations', on_delete=models.CASCADE)