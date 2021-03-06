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


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=64)

    class Meta:
        indexes = [models.Index(fields=['category_name'])]
        ordering = ['category_name']
        verbose_name = 'category_model'
        verbose_name_plural = 'category_models'

    def __str__(self):
        return self.category_name


class IngredientModel(models.Model):
    ingredient_name = models.CharField(max_length=64)
    category = models.ForeignKey(CategoryModel, max_length=64, on_delete=CASCADE)

    class Meta:
        indexes = [models.Index(fields=['ingredient_name'])]
        ordering = ['-ingredient_name']
        verbose_name = 'ingredient_model'
        verbose_name_plural = 'ingredients_model'

    def __str__(self):
        return self.ingredient_name


class OrdersModel(models.Model):
    ingredient_order = models.ManyToManyField('IngredientModel')
    date_order = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.ingredient_order
