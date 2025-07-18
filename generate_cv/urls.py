from django.urls import path
from . import views

app_name = 'generate_cv'
urlpatterns = [
    path('', views.generate, name='index'),
    path('<int:id>/', views.generate, name='view'),
]