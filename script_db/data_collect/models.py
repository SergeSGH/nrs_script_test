from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Record(models.Model):
    num = models.IntegerField(
        '№',
        help_text='№'
    )
    order_num = models.IntegerField(
        'заказ №',
        help_text='заказ №'
    )
    cost = models.IntegerField(
        'стоимость,$',
        help_text='долл. США'
    )
    delivery_date = models.DateField(
        'срок поставки',
        help_text='срок поставки'
    )
    cost_rub = models.DecimalField(
        'стоимость,руб.',
        help_text='стоимость,руб.',
        decimal_places=1,
        max_digits=6
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Запись таблицы заказов'
        verbose_name_plural = 'Записи таблицы заказов'

    def __str__(self):
        return self.order_num
