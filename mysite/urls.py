from django.conf.urls import patterns, include, url
from addr_book.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^index/$',index),
    (r'^library/$',library),
    (r'^book/(\S+)/$',book),
    (r'^search/$',search),
    (r'^addBook/$',addBook),
    (r'^addaBook/$',addBookView),
    (r'^index/(\S+)/$',delete),
    (r'^change/(\S+)/$',change),
    (r'^changeInfo/(\w+)$',update),
    (r'^addAuthor/$',addAuthor),
    (r'^addTodb/$',addTodb),
    (r'^authors/$',authors),
    (r'^$',library),
)
