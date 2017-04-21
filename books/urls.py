from django.conf.urls import url

from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book_detail(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
