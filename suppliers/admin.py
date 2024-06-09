from django.contrib import admin

from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    '''
    Фильтрует по (уровням, названию, продуктам, стране)
    Поиск по (уровню, продукту, стране)
    '''
    list_display = ('pk', 'title', 'country', 'city', 'author', 'levels', 'supply', 'debt', 'creation_date',)
    list_filter = ('levels', 'title', 'product', 'country')
    search_fields = ('levels', 'product__title', 'country')
    actions = ['cleanup_debt']
    list_display_links = ('supply',)

    def cleanup_debt(self, request, queryset):
        '''Очистка задолженности'''
        for supply_object in queryset:
            supply_object.debt = 0
            supply_object.save()
        self.message_user(request, 'Задолженность перед поставщиком у выбранных объектов очищена.')

    cleanup_debt.short_description = 'Очистить задолженность'
