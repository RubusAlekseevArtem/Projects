from django.urls import path

from . import views
from .views import contactView, successView, index

app_name = 'suppliers'

urlpatterns = [
    path('', views.suppliersView, name='suppliers'),
    path("index/", index, name="index"),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
]
