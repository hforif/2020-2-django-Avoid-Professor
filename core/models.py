from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default='사랑의 실천')
    professor = models.CharField(max_length=50, default='송영수')
    del_assistance = models.BooleanField(default=False)
    open_hydrant = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.subject}, {self.professor}'


class Item(models.Model):
    name = models.CharField(max_length=50, default='???')
    bio = models.TextField()
    photo = models.ImageField(blank=True, null=True)

    STATUS_CHOICES = (
        ('AC', '사용하기'),
        ('UN', '현재 장소에서 사용이 불가능한 아이템입니다.'),
        ('AU', '이미 사용한 아이템입니다.')
    )

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.owner}'
