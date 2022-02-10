from unicodedata import name
from django.urls import include , path
from .apiviews import api_payment
from . import views

#nos Chemin d'accès
urlpatterns = [
    path('api/academicians/', views.index , name ='index'),
    path('api/academicians/<int:id>',views.update , name = 'update'),
    # path('api/payments/classement/', views.api_payement_classement),
    # path('api/reasons/' ,views.api_reasons),
    # path('api/reasons/<int:id>', views.api_reasons_details),
    path('', api_payment, name='api_payment'),

]