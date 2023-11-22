from app1.views import *
from django.urls import path
app_name='hai'
urlpatterns=[
    path('person1/',person1,name='person1'),
]