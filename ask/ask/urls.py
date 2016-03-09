from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',

    url(r'^$', 'questions_list', {'name': 'home'}, name='home'),
    url(r'^login/$', 'test', name='login'),
    url(r'^signup/$', 'test', name='signup'),
    url(r'^question/(?P<id>\d+)/$', 'question', name='question'),
    url(r'^ask/$', 'test', name='ask'),
    url(r'^popular/$', 'questions_list', name='popular'),
    url(r'^new/$', 'test', name='new'),

    url(r'^admin/', include(admin.site.urls)),

)

