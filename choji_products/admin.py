from django.contrib import admin
from .models import Choji_products, Choji_offer


class Choji_productsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class Choji_offerAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Choji_products, Choji_productsAdmin)
admin.site.register(Choji_offer, Choji_offerAdmin)
