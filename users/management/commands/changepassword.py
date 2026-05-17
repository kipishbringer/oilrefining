from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Смена пароля пользователя'

    def handle(self, *args, **kwargs):
        name = input('Имя пользователя: ')

        try:
            user = User.objects.get(name=name)

        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Пользователь не найден')
            )
            return

        while True:
            password1 = input('Новый пароль: ')
            password2 = input('Подтвердите пароль: ')

            if password1 == password2:
                break

            print('\nПароли не совпадают.\n')

        user.set_password(password1)
        user.save()

        self.stdout.write(
            self.style.SUCCESS('Пароль успешно изменён')
        )