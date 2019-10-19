from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=100, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.TextField(max_length=50, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return self.text


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answers',  on_delete=models.CASCADE, verbose_name='Опрос' )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    pos_answer = models.ForeignKey('webapp.Choice', related_name='p_answers', on_delete=models.CASCADE,
                                   verbose_name='Вариант ответа')
