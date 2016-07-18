from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # description = models.TextField(null=True, blank=True)
    # ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=0, max_digits=20)
    # old_price = models.DecimalField(decimal_places=0, max_digits=20, null=True, blank=True)
    serial = models.IntegerField(null=True, blank=True)
    image = models.FileField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name



