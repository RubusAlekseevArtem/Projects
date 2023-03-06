from django.urls import path

from .views import response_by_query_name, index

app_name = 'suppliers'

urlpatterns = [
    path("index/", index, name="index"),
    path("index/<str:query_name>", response_by_query_name, name="query_name"),
]
