from django.db import models


class Track(models.Model):

    """Track Model"""

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Subject(models.Model):

    """Major Model"""

    name = models.CharField(max_length=30)
    require = models.BooleanField()
    year = models.IntegerField()
    credit = models.IntegerField()
    track = models.ForeignKey(
        "Track", related_name="track", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
