from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
    )
    list_editable = ('title',)
    search_fields = ('title',)
    list_filter = ('price',)
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
