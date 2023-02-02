from django.urls import path

from .views import index

app_name = 'suppliers'

urlpatterns = [
    path("index/", index, name="index"),
]
