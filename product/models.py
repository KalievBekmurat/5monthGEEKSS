from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)


class Review(models.Model):
    text = models.TextField(max_length=1000,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.text
