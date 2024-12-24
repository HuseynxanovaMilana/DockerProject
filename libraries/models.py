from datetime import datetime

from django.conf import settings
from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    created = models.DateTimeField(verbose_name="Registered Date", null=True, blank=True, editable=False)
    updated = models.DateTimeField(verbose_name="Update Date", null=True, blank=True)

    def save(self, _update=True, *args, **kwargs):
        """ On save, update timestamps """
        # Set time now
        now = datetime.now()
        if not self.id:
            self.created = now
        if _update:
            self.updated = now

        # Super() save User
        super(BookModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "BookModel"
        verbose_name_plural = "BookModels"
