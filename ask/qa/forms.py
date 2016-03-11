# -*- coding: utf-8 -*-

from django import forms

from views import *


class AskForm(forms.Form):
  print 'AskForm'
  title = forms.CharField()
  text = forms.CharField(widget=forms.Textarea)

  def __init__(self, user, **kwargs):
    print '__init__'
    self._user = user
    super(AskForm, self).__init__(**kwargs)

  def save(self):
    if self._user != 'Anonymous':
      pass
#      self.cleaned_data['author'] = self._user
    return Question.objects.create(**self.cleaned_data)



class AnswerForm(forms.Form):
  print 'AnswerForm'
  question = forms.IntegerField(min_value=1)
  text = forms.CharField(widget=forms.Textarea)

  def __init__(self, user, *args, **kwargs):
    self._user = user
    super(AnswerForm, self).__init__(*args, **kwargs)


  def clean_question(self):
    try:
      question = self.cleaned_data['question']
      self._q = Question.objects.get(id=question)
    except:
      raise forms.ValidationError("Нет такого вопроса!")

  def save(self):
    if self._user != 'Anonymous':
      self.cleaned_data['author'] = self._user
    return Answer.objects.create(
      question=self._q,
      **self.cleaned_data
    )












