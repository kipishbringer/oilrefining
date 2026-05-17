from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        name = str(input('Имя пользователя: '))
        while True:
            password1 = str(input('Пароль: '))
            password2 = str(input('Подтвердите пароль: '))
            if password1 == password2:
                password = password2
                break
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.\n')

        user = User.objects.create(
            name=name,
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password(password)
        user.save()

        print('\nПользователь создан.\n')
