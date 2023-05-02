from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

class FastFood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Caffeine(models.Model):
    name = models.CharField(max_length=100)
    drink_type = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    fastfood = models.ForeignKey(FastFood, on_delete=models.CASCADE, null=True, blank=True)
    caffeine = models.ForeignKey(Caffeine, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

