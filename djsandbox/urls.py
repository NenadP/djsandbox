from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'entry.views.index', name='home'),
     url(
         r'^entry/view/(?P<slug>[^\.]+).html',
         'entry.views.view_entry',
         name='view_entry'),
     url(
         r'^entry/category/(?P<slug>[^\.]+).html',
         'entry.views.view_category',
         name='view_entry_category'),

    url(r'^admin/', include(admin.site.urls)),
)
