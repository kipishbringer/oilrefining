from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Subdivision(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="название")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subdivisions')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'


class Brigade(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='brigades')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бригада'
        verbose_name_plural = 'бригады'


class Territory(models.Model):
    TERRITORY_TYPES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('GENERAL', 'Общая'),
    ]

    name = models.CharField(max_length=255, verbose_name='название')
    territory_type = models.CharField(max_length=20, choices=TERRITORY_TYPES)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='territories')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'территория'
        verbose_name_plural = 'территории'


class BrigadeTerritoryAssignment(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, related_name='territory_assignments',
                                verbose_name="бригада")
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE, related_name='brigade_assignments',
                                  verbose_name="территория")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brigade.name} принадлежит {self.territory.name}'

    class Meta:
        verbose_name = 'принадлежность'
        verbose_name_plural = 'принадлежности'


class Position(models.Model):
    DEVICE_TYPES = [
        ('manometer', 'манометр'),
        ('thermometer', 'термометр'),
    ]

    name = models.CharField(max_length=255, verbose_name='название')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='positions',
                                    verbose_name='подразделение')
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE, related_name='positions',
                                  verbose_name='территория')
    device_type = models.CharField(max_length=20,choices=DEVICE_TYPES, verbose_name='тип позиции')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'


class Manometer(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='manometers',
                                 verbose_name="позиция")
    next_verification_date = models.DateField(verbose_name="дата следующей поверки")
    serial_number = models.CharField(max_length=255, unique=True, verbose_name="заводской номер")
    scale = models.CharField(max_length=255, verbose_name="шкала измерения")
    unit = models.CharField(max_length=50, verbose_name="единица измерения")
    notes = models.TextField(verbose_name="примечания", **NULLABLE)
    is_working = models.BooleanField(default=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='manometers',
                                    verbose_name="подразделение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="комплекс")


class Thermometer(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='thermometers',
                                 verbose_name="позиция")
    next_verification_date = models.DateField(verbose_name="дата следующей поверки")
    serial_number = models.CharField(max_length=255, unique=True, verbose_name="заводской номер")
    scale = models.CharField(max_length=255, verbose_name="шкала измерения")
    unit = models.CharField(max_length=50, verbose_name="единица измерения")
    notes = models.TextField(verbose_name="примечания", **NULLABLE)
    is_working = models.BooleanField(default=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='thermometers',
                                    verbose_name="подразделение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="комплекс")



"""ТРЕШ"""
# class Position(models.Model):
#
#     class Group(models.TextChoices):
#         A = 'A', 'группа A'
#         B = 'B', 'группа B'
#         C = 'C', 'группа C'
#         D = 'D', 'группа D'
#         GENERAL = 'GENERAL', 'Общая'
#
#     name = models.CharField(max_length=255, unique=True, verbose_name='название')
#     group = models.CharField(max_length=20, choices=Group.choices, default=Group.GENERAL, verbose_name='группа')
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
#                                related_name='positions', verbose_name='подразделение')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'позиция'
#         verbose_name_plural = 'позиции'
#
#
# class Manometer(models.Model):
#
#     position = models.OneToOneField('Position', on_delete=models.SET_NULL, to_field='name', unique=True,
#                                  related_name='manometers', verbose_name='позиция', **NULLABLE)
#     next_verification_date = models.DateField(verbose_name='дата следующей поверки')
#     serial_number = models.CharField(max_length=50, unique=True, verbose_name='серийный номер')
#     scale = models.CharField(max_length=30, verbose_name='шкала')
#     unit = models.CharField(max_length=25, verbose_name='единица измерения')
#     notes = models.TextField(verbose_name='примечания', **NULLABLE)
#     is_working = models.BooleanField(default=True, verbose_name='статус исправности')
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
#                                related_name='manometers', verbose_name='подразделение')
#
#     def __str__(self):
#         return f'манометр {self.serial_number}'
#
#     class Meta:
#         verbose_name = 'манометр'
#         verbose_name_plural = 'манометры'
#
#
# class Thermometer(models.Model):
#
#     position = models.OneToOneField('Position', on_delete=models.SET_NULL, to_field='name', unique=True,
#                                  related_name='thermometers', verbose_name='позиция', **NULLABLE)
#     next_verification_date = models.DateField(verbose_name='дата следующей поверки')
#     serial_number = models.CharField(max_length=50, unique=True, verbose_name='серийный номер')
#     scale = models.CharField(max_length=30, verbose_name='шкала')
#     unit = models.CharField(max_length=25, default='°C', verbose_name='единица измерения')
#     notes = models.TextField(verbose_name='примечания', **NULLABLE)
#     is_working = models.BooleanField(default=True, verbose_name='статус исправности')
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
#                                related_name='thermometers', verbose_name='подразделение')
#
#     def __str__(self):
#         return f'термометр {self.serial_number}'
#
#     class Meta:
#         verbose_name = 'термометр'
#         verbose_name_plural = 'термометры'