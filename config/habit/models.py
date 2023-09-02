import django
from django.conf import settings
from django.db import models



NULLABLE = {'blank': True, 'null': True}

class Habit(models.Model):

    USER_PERIOD_CHOICE = [
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно')

    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец привычки')
    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_enjoyable = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.CharField(choices=USER_PERIOD_CHOICE, max_length=10, verbose_name='периодичность')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)
    lead_time = models.TimeField(default='00:05:00', verbose_name='время выполнения')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')



    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'