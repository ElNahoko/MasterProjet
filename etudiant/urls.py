from django.conf.urls import url
from . import views

from .views import (StudentCreateView, StudentListView, StudentUpdateView, StudentDeleteView)

app_name = 'etudiant'

urlpatterns = [
    url('list', StudentListView.as_view(), name='student_list'),
    url('create/', StudentCreateView.as_view(), name='etudiant_create'),
    url('(?P<pk>[0-9]+)/delete/$', StudentDeleteView.as_view(), name='student_delete'),
    url('(?P<pk>[0-9]+)/update/$', StudentUpdateView.as_view(), name='student_update'),
]