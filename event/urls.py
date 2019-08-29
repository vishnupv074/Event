from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('about_view', views.about_view, name='about_view'),
    path('contact_view', views.contact_view, name='contact_view'),
    path('register_view', views.register_view, name='register_view'),
]
