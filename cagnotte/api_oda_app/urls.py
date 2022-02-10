from unicodedata import name
from django.urls import include, path
from . import views
 
#nos Chemin d'accès
urlpatterns = [
    path('api/academicians/', views.api_academicain , name ='api_academicain'),
    path('api/academicians/<str:register_number>',views.api_academicain_update , name = 'update'),
    # path('api/payments/classement/', views.api_payement_classement),
    # path('api/reasons/' ,views.api_reasons),
    # path('api/reasons/<int:id>', views.api_reasons_details),
]