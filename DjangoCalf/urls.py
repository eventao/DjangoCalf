from django.conf.urls import url
from . import view, testdb

urlpatterns = [
    url(r'^$', view.home),
    url(r'^about$', view.about),
    url(r'^contact$', view.contact),
    url(r'^testdb', testdb.testdb),
]
