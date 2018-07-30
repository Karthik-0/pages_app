from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.text import slugify


class Page(TimeStampedModel):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    content = models.TextField()
    ordering = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
