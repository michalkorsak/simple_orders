from django.contrib import admin
from app.models import UserProfileInfo, IngredientModel, OrdersModel

admin.site.register(UserProfileInfo)
admin.site.register(IngredientModel)
admin.site.register(OrdersModel)