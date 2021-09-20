from django.urls import path
from .views import Studentlist

urlpatterns=[
    path('show/',Studentlist.as_view(),name='show')
]