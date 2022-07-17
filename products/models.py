from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120, null=False)
    contetnt = models.TextField(null=True,blank=True)
    price =models.DecimalField(max_digits=15, decimal_places=2, default=0.0)

    @property
    def sale(self):
        return 4+self.price*5

    def discount_is(self):
        return 500