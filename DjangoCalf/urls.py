from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^$', view.home),
    url(r'^about$', view.about),
    url(r'^contact$', view.contact),
]
