# -*- coding: utf-8 -*-

from django import forms

from views import *


class AskForm(forms.Form):
  title = forms.CharField()
  text = forms.CharField(widget=forms.Textarea)

#  def __init__(self, user, *opt):
#    self._user = user
#    super(AskForm, self).__init__(*opt)

#  def save(self, user):
  def save(self):
#    self.cleaned_data['author'] = self._user
#    self.cleaned_data['author'] = user
    return Question.objects.create(**self.cleaned_data)



class AnswerForm(forms.Form):
  question = forms.IntegerField(min_value=1)
  text = forms.CharField(widget=forms.Textarea)

#  def __init__(self, user, *opt):
#    self._user = user
#    super(AnswerForm, self).__init__(*opt)


  def clean_question(self):
    try:
      question = self.cleaned_data['question']
      self._q = Question.objects.get(id=question)
    except:
      raise forms.ValidationError("Нет такого вопроса!")

#  def save(self, user):
  def save(self):
    pass
    return Answer.objects.create(
      question=self._q,
      text=self.cleaned_data['text'],
#      author=self._user
#      author=user
    )












