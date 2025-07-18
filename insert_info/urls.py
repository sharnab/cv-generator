from django.urls import path
from . import views

app_name = 'insert_info'
urlpatterns = [
    path('', views.insert, name='index'),
    path('save/', views.insert_info, name='save'),
]