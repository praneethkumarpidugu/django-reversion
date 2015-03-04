from django.conf.urls import patterns, url


urlpatterns = patterns('rev_history.views',
    url(r'^history/$', 'history_list', name='history-list'),
)
