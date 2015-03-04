from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^', include('app1.urls', namespace='app1')),
    url(r'^', include('rev_history.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
