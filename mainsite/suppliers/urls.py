from django.urls import path

from mainsite.suppliers.views import index, response_by_query_name

app_name = 'suppliers'

urlpatterns = [
    path("index/", index, name="index"),
    path("index/<str:query_name>", response_by_query_name, name="query_name"),
]
