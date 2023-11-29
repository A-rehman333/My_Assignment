
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('index/', admin.site.urls),
    path('', views.index),

    path('index/', views.show, name='show'),
    path('show/', views.show, name='show'),
]
