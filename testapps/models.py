from django.db import models


class AiNotice(models.Model):

    """Ai Notice Definition"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    number = models.IntegerField()
    date = models.DateTimeField()
    link = models.URLField()

    class Meta:
        verbose_name = "Ai Notice"


class ComNotice(models.Model):

    """Com Notice Definition"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    number = models.IntegerField()
    date = models.DateTimeField()
    link = models.URLField()

    class Meta:
        verbose_name = "Computer Notice"
