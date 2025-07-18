from django.urls import path
from . import views

app_name = 'update_info'
urlpatterns = [
    path('', views.update, name='index'),
]