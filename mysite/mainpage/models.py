from django.db import models

class Products(models.Model):
    name_product = models.CharField('Назва',max_length=250)
    price_product = models.IntegerField('Ціна')
    about_product = models.TextField('Опис')
    date = models.DateTimeField('Дата добавлення',auto_now_add=True)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name="Товар"
        verbose_name_plural = 'Товари'


