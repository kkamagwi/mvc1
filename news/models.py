import datetime
from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.tag

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    create = models.DateTimeField(default=datetime.datetime.now, blank=True)
    img_url = models.URLField()
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True,)

    def __str__(self) -> str:
        return self.title
