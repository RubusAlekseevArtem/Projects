from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.SuppliersView.as_view(), name='suppliers')
]
