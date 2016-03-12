from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',

    url(r'^$', 'questions_list', name='home'),
    url(r'^login/$', 'login', {'template_name':'login.html'}, name='login'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^question/(?P<id>\d+)/$', 'question', name='question'),
    url(r'^ask/$', 'ask', name='ask'),
    url(r'^answer/$', 'answer', name='answer'),
    url(r'^popular/$', 'questions_list', name='popular'),
    url(r'^new/$', 'test', name='new'),

    url(r'^admin/', include(admin.site.urls)),

)
