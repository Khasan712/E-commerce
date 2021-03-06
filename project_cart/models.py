from django.db import models
from mainapp.models import Product
from custom_user.models import Custom_User
# product_qty = Product.objects.all()


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    # def get_cart_count(self):
    #     return self.cart.count()

class CartItem(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='cart')
    quantity = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product)

    def get_total_cart_item_price(self):
        return (self.product.price * self.quantity)

    def get_total_cart_price(self):
        pass

    def get_cart_count(self):
        return self.cart.count()