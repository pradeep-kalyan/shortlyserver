from django.db import models
import random, string


# Create your models here.
def generate_short():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


class ShortUrl(models.Model):
    org_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=6, unique=True, default=generate_short)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} -> {self.org_url}"
