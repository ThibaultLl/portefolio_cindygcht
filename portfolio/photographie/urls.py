from django.urls import path

from . import views

app_name = 'photographie'
urlpatterns = [
    path('', views.photographie, name='photographie'),
]