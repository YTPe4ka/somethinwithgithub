from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    unit_price=models.DecimalField(decimal_places=2, max_digits=10)
    discounted=models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
         return self.product_name

class Orders(models.Model):
    order_date=models.DateTimeField()
    required_date=models.DateTimeField()
    shipped_date=models.DateTimeField()
    def __str__(self):
        return f"Order #{self.id}"

class OrderDetails(models.Model):
    order=models.ForeignKey(Orders, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    unit_price=models.DecimalField(decimal_places=2, max_digits=10)
    quantity=models.IntegerField()
    discounted=models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return f"{self.product.product_name} — {self.quantity} dona"



class Employee(models.Model):
    employee_id=models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



