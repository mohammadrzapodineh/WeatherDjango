from django.urls import path
from .views import weather
app_name = 'Weather'
urlpatterns = [
    path('', weather, name='home_page')
]