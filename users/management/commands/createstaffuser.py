from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a new staff user.'

    def handle(self, *args, **kwargs):
        user = get_user_model()

        email = input("Email: ")
        password = input("Password: ")

        if user.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR('user with this email already exists.'))
        else:
            user = user.objects.create_staffuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Staff user {user.email} created successfully.'))
