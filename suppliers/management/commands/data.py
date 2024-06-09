from colorama import Fore
from django.core.management import BaseCommand
from products.models import Product
from suppliers.models import Supplier
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()

        if Product.objects.filter(title='Телевизор', model='Samsung') and Product.objects.filter(title='Микрофон',
                                                                                                 model='Rock'):
            pass
        else:
            products1 = Product.objects.create(title='Телевизор', model='Samsung')
            products1.save()

            products2 = Product.objects.create(title='Микрофон', model='Rock')
            products2.save()

        for user in users:
            dict_suppliers = {
                'suppliers1': {
                    'title': 'ОАО "Созвездие"',
                    'email': f'{user.pk}Constellation@mail.ru',
                    'country': 'Россия',
                    'city': 'Москва',
                    'street': 'Кирова',
                    'house': '5',

                    'debt': 1000,
                },

                'suppliers2': {
                    'title': 'ИП "Воронов"',
                    'email': f'{user.pk}Voronov@gmail.com',
                    'country': 'Россия',
                    'city': 'Рязань',
                    'street': 'Ленина',
                    'house': '24',

                    'levels': 2,
                    'debt': 345,
                },

                'suppliers3': {
                    'title': 'Шанхайская организация сотрудничества',
                    'email': f'{user.pk}sectsco@mail.com',
                    'country': 'Китай',
                    'city': 'Шанхай',
                    'street': 'Ли',
                    'house': '7',

                    'levels': 1,
                    'debt': 302,
                },
            }

            try:
                for row in dict_suppliers:
                    route = Supplier.objects.create(**dict_suppliers[row])
                    route.supply = route
                    route.product.add(products1, products2)
                    route.save()
                    print(f'Пользователь: {Fore.GREEN}{user}{Fore.RESET} создал 1 поставщика!')

            except Exception as e:
                print(f'{Fore.RED}Возникла ошибка при создании поставщика\n{Fore.RESET}{e}')
