from django.urls import path
from . import views

app_name = 'delete_info'
urlpatterns = [
    path('<int:id>/', views.delete, name='delete'),
]