from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        print('\nsuperuser')
        while True:
            password1 = str(input('Пароль: '))
            password2 = str(input('Подтвердите пароль: '))
            if password1 == password2:
                password = password2
                break
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.\n')

        user = User.objects.create(
            name='superuser',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(password)
        user.save()

        print('\nКГОДТ')
        while True:
            password1 = str(input('Пароль: '))
            password2 = str(input('Подтвердите пароль: '))
            if password1 == password2:
                password = password2
                break
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.\n')

        user = User.objects.create(
            name='КГОДТ',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password(password)
        user.save()

        print('\nОЗХ')
        while True:
            password1 = str(input('Пароль: '))
            password2 = str(input('Подтвердите пароль: '))
            if password1 == password2:
                password = password2
                break
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.\n')

        user = User.objects.create(
            name='ОЗХ',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password(password)
        user.save()

        print('\nУПВ')
        while True:
            password1 = str(input('Пароль: '))
            password2 = str(input('Подтвердите пароль: '))
            if password1 == password2:
                password = password2
                break
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.\n')

        user = User.objects.create(
            name='УПВ',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password(password)
        user.save()
        print('\nПользователи созданы.\n')
