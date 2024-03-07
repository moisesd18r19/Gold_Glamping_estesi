
from . import views
from django.urls import path

urlpatterns = [       
               
        path('', views.pagos, name='pagos'),   
        path('pago_status_/<int:pago_id>/', views.change_status_pago, name='pago_status'),            
       
        path('create/', views.create_pagos, name='create_pagos'), 
        path('detail/<int:pago_id>/', views.detail_pago, name='detail_pago'),  
        path('delete/<int:pago_id>/', views.delete_pago, name='delete_pago'),
        path('edit/<int:pago_id>/', views.edit_pago, name='edit_pago'),
        path('', views.index, name='pagos'),
        path('pago_reserva/<int:id>/', views.pago_reserva, name='pago_reserva'),	

    ]