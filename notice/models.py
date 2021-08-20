from django.db import models


class AiNotice(models.Model):

    """Ai Notice Definition"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    number = models.IntegerField()
    date = models.DateField()
    link = models.URLField()
    specific_id = models.IntegerField()

    class Meta:
        verbose_name = "Ai Notice"


class ComNotice(models.Model):

    """Com Notice Definition"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    number = models.IntegerField()
    date = models.DateField()
    link = models.URLField()
    specific_id = models.IntegerField()

    class Meta:
        verbose_name = "Computer Notice"
