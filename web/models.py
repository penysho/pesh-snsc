from django.db import models
from django.utils import timezone


class Site(models.Model):

    site_id = models.BigAutoField(primary_key=True)
    site_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "site"

    def __str__(self):
        return self.site_id
