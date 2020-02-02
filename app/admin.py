from django.contrib import admin
from app.models import UserProfileInfo, IngredientModel, OrdersModel, CategoryModel

admin.site.register(UserProfileInfo)
admin.site.register(IngredientModel)
admin.site.register(CategoryModel)
admin.site.register(OrdersModel)