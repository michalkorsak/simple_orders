from django.contrib import admin
from app.models import UserProfileInfo, IngredientModel, MenuModel, OrdersModel

admin.site.register(UserProfileInfo)
admin.site.register(IngredientModel)
admin.site.register(MenuModel)
admin.site.register(OrdersModel)