from django.core.management import BaseCommand
from app_shops.models import Shop


class Command(BaseCommand):
    help = 'Добавить 1000 магазинов'

    def handle(self, *args, **options):
        for i in range(1, 21):
            Shop.objects.create(name=f'Магазин {i}')

        self.stdout.write('Магазины успешно загружены')
