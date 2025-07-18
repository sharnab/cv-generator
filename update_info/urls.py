from django.urls import path
from . import views

app_name = 'update_info'
urlpatterns = [
    path('<int:id>/', views.update, name='edit'),
    path('save/', views.update_info, name='save'),
]