# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
  title = models.TextField('заголовок вопроса') # заголовок вопроса
  text = models.TextField('полный текст вопроса') # полный текст вопроса
  added_at = models.DateTimeField('дата добавления вопроса') # дата добавления вопроса
  rating = models.IntegerField('рейтинг вопроса (число)') # рейтинг вопроса (число)
  author = models.ForeignKey(User, related_name='question_set_1', verbose_name='автор вопроса') # автор вопроса
  likes = models.ManyToManyField(User,  verbose_name='список пользователей, поставивших "лайк"') # список пользователей, поставивших "лайк"

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return '/question/%d/' % self.pk


class Answer(models.Model):
  text = models.TextField('текст ответа') # текст ответа
  added_at = models.DateTimeField('дата добавления ответа') # дата добавления ответа
  question = models.ForeignKey(Question, verbose_name='вопрос, к которому относится ответ') # вопрос, к которому относится ответ
  author = models.ForeignKey(User, verbose_name='автор ответа') # автор ответа

  def get_absolute_url(self):
    return '/question/%d/' % self.pk
