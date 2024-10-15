from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Menu/')

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Menu, related_name='orders')

    def total_cost(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"ID: {self.id}   Name: {self.customer_name}  Date: {self.order_date}"

