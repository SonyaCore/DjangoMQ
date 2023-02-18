import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

        if not User.objects.filter(username=DJANGO_SU_NAME).exists():
            print("\u001b[32mCreating account for %s (%s)\u001b[0m" % (DJANGO_SU_NAME, DJANGO_SU_EMAIL))
            admin = User.objects.create_superuser(
                email=DJANGO_SU_EMAIL, username=DJANGO_SU_NAME, password=DJANGO_SU_PASSWORD)
            admin.is_active = True
            admin.is_staff = True
            admin.save()
        else:
            print("\u001b[32mAdmin account has already been initialized.\u001b[0m")