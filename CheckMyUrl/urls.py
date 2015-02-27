from urlchecker import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'urlchecker.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^checkit/', 'urlchecker.views.checking'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'home.views.index'),
    #url(,include()),
)

