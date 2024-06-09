from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'blank': True,
    'null': True,
}


class UserRoles(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractUser):
    '''Модель пользователя'''
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    photo = models.ImageField(upload_to='users', verbose_name='Фото', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
