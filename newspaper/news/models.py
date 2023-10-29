from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='articles')

    def __str__(self) -> str:
        return f'{self.owner} | {self.title}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_authtoken(sender, **kwargs):
    if kwargs['created']:
        Token.objects.create(user=kwargs['instance'])