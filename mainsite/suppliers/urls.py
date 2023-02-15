from django.urls import path

from .views import index

app_name = 'suppliers'

urlpatterns = [
    path("index/", index, name="index"),
    path("index/<str:supplier_name>", index, name="suppliers_params"),
]
