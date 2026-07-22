from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Link(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="links")
    url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=6, null=True, db_index=True)
    clicks = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url[:10]}... -> {self.short_code}"

    def is_expired(self):
        now = timezone.now()
        return now > self.expires_at

    def is_valid(self):
        return self.is_active and not self.is_expired()
