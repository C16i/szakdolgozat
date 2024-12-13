from django.db import models
from django.contrib.auth.models import User

class Termek(models.Model):
    Azon = models.CharField(max_length=10)
    Nev = models.CharField(max_length=100)
    Kategoria = models.CharField(max_length=50)
    Kiszereles = models.CharField(max_length=10)
    Ar=models.IntegerField()
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',on_delete=models.CASCADE)
    product= models.ForeignKey('Termek', on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def get_total_price(self):
        return self.product.Ar * self.quantity

