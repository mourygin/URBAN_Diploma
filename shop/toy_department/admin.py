from django.contrib import admin
from .models import Category, Toy, Action, Buyer, Basket

# Класс администрирования товаров (игрушек)


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('title', 'articul', 'cost', 'in_stock',)
    search_fields = ('title', 'articul',)

# Класс администрирования акций


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_date', 'last_date', 'actual',)
    search_fields = ('title', 'first_date', 'last_date')
    ordering = ('first_date',)

# Класс администрирования клиентов


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance',)
    search_fields = ('name',)

# Класс администрирования покупок


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('buyer_id', 'toy_name',)
    search_fields = ('buyer_id', 'toy_name',)
