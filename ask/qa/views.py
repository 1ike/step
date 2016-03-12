# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.contrib.auth.models import User


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

  form = get_answer_form(request)

  return render(request, 'q.html', {
      'q' : q,
      'a' : a,
      'form' : form,
      'user': request.user
  })

def answer(request):
  print 'answer'
  form = get_answer_form(request)

  try:
    form.q_id
    return HttpResponseRedirect('/question/'+str(form.q_id)+'/')
  except:
    return render(request, 'q.html', {
        'form' : form,
        'user': request.user
    })



def get_answer_form(request):
  print 'get_answer_form'
  if request.method == 'POST':
    form = AnswerForm(request.POST)
    if form.is_valid():
      new_a = form.save(request.user)
      form = AnswerForm()
      form.greeting = "Аффтар, пишы ищо!"
      form.q_id = new_a.question_id
    return form
  else:
    return AnswerForm()



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
  if request.method == 'POST':
    form = AskForm(request.POST)
    if form.is_valid():
      q = form.save(request.user)
      return HttpResponseRedirect('/question/'+str(q.id)+'/')
  else:
    form = AskForm()

  return render(request, 'ask.html', {'form': form, 'user': request.user})



def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return HttpResponseRedirect('/')
  else:
    form = SignupForm()

  return render(request, 'signup.html', {'form': form})





