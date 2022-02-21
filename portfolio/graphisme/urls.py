from django.urls import path

from . import views

app_name = 'graphisme'
urlpatterns = [
    path('', views.graphisme, name='graphisme'),
]