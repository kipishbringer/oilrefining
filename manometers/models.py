from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Position(models.Model):

    class Group(models.TextChoices):
        A = 'A', 'группа A'
        B = 'B', 'группа B'
        C = 'C', 'группа C'
        D = 'D', 'группа D'
        GENERAL = 'GENERAL', 'Общая'

    name = models.CharField(max_length=255, unique=True, verbose_name='название')
    group = models.CharField(max_length=20, choices=Group.choices, default=Group.GENERAL, verbose_name='группа')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='positions', verbose_name='подразделение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'


class Manometer(models.Model):

    position = models.OneToOneField('Position', on_delete=models.SET_NULL, to_field='name', unique=True,
                                 related_name='manometers', verbose_name='позиция', **NULLABLE)
    next_verification_date = models.DateField(verbose_name='дата следующей поверки')
    serial_number = models.CharField(max_length=50, unique=True, verbose_name='серийный номер')
    scale = models.CharField(max_length=30, verbose_name='шкала')
    unit = models.CharField(max_length=25, verbose_name='единица измерения')
    notes = models.TextField(verbose_name='примечания', **NULLABLE)
    is_working = models.BooleanField(default=True, verbose_name='статус исправности')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='manometers', verbose_name='подразделение')

    def __str__(self):
        return f'манометр {self.serial_number}'

    class Meta:
        verbose_name = 'манометр'
        verbose_name_plural = 'манометры'


class Thermometer(models.Model):

    position = models.OneToOneField('Position', on_delete=models.SET_NULL, to_field='name', unique=True,
                                 related_name='thermometers', verbose_name='позиция', **NULLABLE)
    next_verification_date = models.DateField(verbose_name='дата следующей поверки')
    serial_number = models.CharField(max_length=50, unique=True, verbose_name='серийный номер')
    scale = models.CharField(max_length=30, verbose_name='шкала')
    unit = models.CharField(max_length=25, default='°C', verbose_name='единица измерения')
    notes = models.TextField(verbose_name='примечания', **NULLABLE)
    is_working = models.BooleanField(default=True, verbose_name='статус исправности')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='thermometers', verbose_name='подразделение')

    def __str__(self):
        return f'термометр {self.serial_number}'

    class Meta:
        verbose_name = 'термометр'
        verbose_name_plural = 'термометры'