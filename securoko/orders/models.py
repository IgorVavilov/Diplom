from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from users.models import Profile
from phonenumber_field.modelfields import PhoneNumberField
from shop.utils import validate_name


class Order(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=20, verbose_name='Имя', null=True, blank=True,
                                  validators=[validate_name], )
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия', validators=[validate_name],)
    email = models.EmailField()
    phone_number = PhoneNumberField('Телефон', max_length=20, default='', null=True, blank=True, region='RU')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    postal_code = models.IntegerField(verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    paid = models.BooleanField(default=False, verbose_name='Оплата')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ # {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT, verbose_name='Заказанный товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
