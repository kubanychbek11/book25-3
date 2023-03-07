from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
(ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER")
)


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользоватнля')
    phone_number = models.CharField('Номер телефона', max_length=20)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')