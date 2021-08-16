from django.db import models


class AiData(models.Model):

    """Ai Data Definition"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateTimeField()
    link = models.URLField()


class ComData(models.Model):

    """Com Data Definition"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateTimeField()
    link = models.URLField()
