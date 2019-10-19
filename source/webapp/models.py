from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')


class Choice(models.Model):
    text = models.CharField(max_length=50, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос')

