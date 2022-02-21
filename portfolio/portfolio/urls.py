from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from home import views
urlpatterns = [
    path('home/', include('home.urls')),
    path('photographie/', include('photographie.urls')),
    path('graphisme/', include('graphisme.urls')),
    re_path('^$',views.accueil,name='home'),
    path('admin/', admin.site.urls),
]
