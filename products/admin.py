from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Фильтр по (автору и названию)
    Поиск по (названию)
    '''
    list_display = ('pk', 'title', 'model', 'release_date', 'author')
    list_filter = ('title', 'author',)
    search_fields = ('title',)
