from django.urls import path
from .apiviews import api_payment

urlpatterns = [
    path('', api_payment, name='api_payment')
]