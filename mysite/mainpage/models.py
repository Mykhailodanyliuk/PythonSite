from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Products(models.Model):
    name_product = models.CharField('Назва', max_length=250)
    price_product = models.IntegerField('Ціна')
    about_product = models.TextField('Опис')
    date = models.DateTimeField('Дата добавлення', default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор',blank=True,null=True)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товари'


