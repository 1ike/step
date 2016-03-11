# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import *
from django.contrib.auth.decorators import login_required


from models import * #Question, Answer
from forms import *



def test(request, *args, **kwargs):
  return render_to_response('h.html')
#  return HttpResponse('OK')



def question(request, id):
  print 'question'
  q = get_object_or_404(Question, id=id)
  try:
    a = Answer.objects.filter(question=id)[:]
  except Answer.DoesNotExist:
    a = none

  user = set_user(request.user)

  form = get_answer_form(user, request)

  return render(request, 'q.html', {
      'q' : q,
      'a' : a,
      'form' : form,
      'user': user
  })

def answer(request):
  print 'answer'
  user = set_user(request.user)

  form = get_answer_form(user, request)

  try:
    form.q_id
    return HttpResponseRedirect('/question/'+str(form.q_id)+'/')
  except:
    return render(request, 'q.html', {
        'form' : form,
        'user': user
    })



def get_answer_form(user, request):
  print 'get_answer_form'
  if request.method == 'POST':
    form = AnswerForm(user, request.POST)
    if form.is_valid():
      new_a = form.save()
      form = AnswerForm(user)
      form.greeting = "Аффтар, пишы ищо!"
      form.q_id = new_a.question_id
    return form
  else:
    return AnswerForm(user)

def set_user(user):
  print 'set_user'
  if not user.is_authenticated():
    user = 'Anonymous'
  return user



def questions_list(request, **opt):
  print 'questions_list'
  qs = Question.objects
  try:
    opt['name']
    qs = qs.all()
    baseurl = '/?page='
  except:
    qs = qs.order_by('-rating')
    baseurl = '/popular/?page='

  page = paginate(request, qs)

  return render(request, 'qs.html', {
      'posts' : page.object_list,
      'page' : page,
  })


def paginate(request, qs):
  print 'paginate'
  try:
    limit = int(request.GET.get('limit', 10))
  except ValueError:
    limit = 10
  if limit > 100:
    limit = 10
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  paginator = Paginator(qs, limit)
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return page



def ask(request):
  print 'ask'
  user = set_user(request.user)

  if request.method == 'POST':
    form = AskForm(user, request.POST)
    if form.is_valid():
      q = form.save()
      print str(q.id)
      return HttpResponseRedirect('/question/'+str(q.id)+'/')
  else:
    form = AskForm(user)

  return render(request, 'ask.html', {'form': form, 'user': user})





