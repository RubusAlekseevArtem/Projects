from django.urls import path

from . import views
from .views import contactView, successView, index
from django.conf.urls.static import static
from django.conf import settings

app_name = 'suppliers'

urlpatterns = [
    path('', views.suppliersView, name='suppliers'),
    path("index/", index, name="index"),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
