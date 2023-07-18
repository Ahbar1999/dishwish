from django.db import models

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    location = models.TextField()

class Dish(models.Model):
    name = models.TextField(primary_key=True)
    price = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
