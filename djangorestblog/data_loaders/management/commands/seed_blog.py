from data_loaders.management.commands._data import seed_blog
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Load basic data"

    def handle(self, *args, **options):
        seed_blog()
