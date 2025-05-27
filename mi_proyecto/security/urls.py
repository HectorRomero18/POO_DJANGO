# urls.py
from django.urls import path
from .views import menu_detail


urlpatterns = [
    path('menu/<int:id>/', menu_detail, name='menu_detail'),
]
