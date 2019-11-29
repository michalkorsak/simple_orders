from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import CASCADE


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class IngredientModel(models.Model):
    ingredient_name = models.CharField(max_length=64)

    def __str__(self):
        return self.ingredient_name


class MenuModel(models.Model):
    dish_name = models.CharField(max_length=64)
    ingredient_menu = models.ManyToManyField(IngredientModel)

    def __str__(self):
        return self.dish_name


class OrdersModel(models.Model):
    ingredient_order = models.ManyToManyField(IngredientModel)
    date_order = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.ingredient_order
