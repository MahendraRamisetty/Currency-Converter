from django.urls import path
from .views import currency_converter_view

urlpatterns = [
    path('',currency_converter_view ),
]