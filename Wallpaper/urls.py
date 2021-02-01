from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('checkNewImage', views.check_new_image, name = 'check_new_image'),
]
