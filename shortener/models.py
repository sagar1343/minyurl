from django.db import models

# Create your models here.


class Links(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=6)
    click_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url[:10]}... -> {self.short_code}"
