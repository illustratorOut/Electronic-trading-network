from django.db import models
from django.utils import timezone
from products.models import Product
from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}


class Levels(models.IntegerChoices):
    FACTORY = 0, 'Завод'
    RETAIL_NETWORK = 1, 'Розничная сеть'
    IP = 2, 'Индивидуальный предприниматель'


class Supplier(models.Model):
    '''Модель поставщика'''
    title = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Эл. почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='№ дома')

    product = models.ManyToManyField(Product, verbose_name='Продукт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поставщика', **NULLABLE)
    supply = models.ForeignKey('Supplier', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)

    levels = models.IntegerField(choices=Levels.choices, default=Levels.FACTORY, verbose_name='Уровень структуры')
    debt = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Задолженность', **NULLABLE)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return f'Название: ({self.title}) - Уровень структуры: ({self.levels})'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
