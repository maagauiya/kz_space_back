from django.urls import path

from .views import*

urlpatterns=[
    path('one/',page1,name='main page'),
    path('two/',page2,name='main page'),
    path('',page3,name='main page'),
    path('four/',page4,name='main page'),
    path('five/',page5,name='main page'),
    path('six/',page6,name='main page'),
    path('document/<int:pk>',document,name="document")
]