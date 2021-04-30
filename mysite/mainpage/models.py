from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Products(models.Model):
    name_product = models.CharField('Назва',max_length=250)
    price_product = models.IntegerField('Ціна')
    about_product = models.TextField('Опис')
    date = models.DateTimeField('Дата добавлення', default=timezone.now)
    # author = models.ForeignKey(User, null=True, blank=True,editable=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name="Товар"
        verbose_name_plural = 'Товари'


