from django.urls import path
from .views import subscribe1
urlpatterns = [
    path('', subscribe1, name='subscribe'),
]
