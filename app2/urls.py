from app2.views import *
from django.urls import path
app_name='hello'
urlpatterns=[
    path('person2/',person2,name='person2')
]
