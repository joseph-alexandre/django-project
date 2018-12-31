from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('test', views.view_test, name='view_test')
]