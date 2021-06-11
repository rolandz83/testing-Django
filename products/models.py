from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2,max_digits=100)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(default='This is cool!')

    def get_abs_url(self):
        return f"/products/{self.id}"
