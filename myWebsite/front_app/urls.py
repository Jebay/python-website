from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^fruit/(?P<fruit>\w+)', views.fruit, name='fruit'),
    url(r'^vegetable/(?P<vegetable>\w+)', views.vegetable, name='vegetable'),
    url(r'', views.home, name='home'),
]
