from django.db import models
from suppliers.models import NULLABLE
from django.utils import timezone

from users.models import User


class Product(models.Model):
    '''Модель продукта'''
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор продукта', **NULLABLE)

    def __str__(self):
        return f'Название продукта: ({self.title}) Модель продукта: ({self.model})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
