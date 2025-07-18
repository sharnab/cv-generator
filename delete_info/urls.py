from django.urls import path
from . import views

app_name = 'delete_info'
urlpatterns = [
    path('', views.delete, name='index'),
]