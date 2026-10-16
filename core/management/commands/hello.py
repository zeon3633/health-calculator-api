from django.core.management.base import BaseCommand
from django.contrib.auth.models import User 

class Command(BaseCommand):
    help = 'Создает нового пользователя в базе данных'

    def handle(self, *args, **options):
        username = "ivan_python"
        email = "ivan@example.com"
        password = "SuperPassword123"

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Пользователь {username} успешно создан!"))
        else:
            self.stdout.write(self.style.WARNING(f"Пользователь {username} уже существует."))
