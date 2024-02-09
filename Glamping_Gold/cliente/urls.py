from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cliente, name='cliente'),     
    path('cliente_status/<int:cliente_id>/', views.change_status_cliente, name='cliente_status'),  
    path('create/', views.create_cliente, name='create_cliente'),  
    path('detail/<int:cliente_id>/', views.detail_cliente, name='detail_cliente'), 
    path('delete/<int:cliente_id>/', views.delete_cliente, name='delete_cliente'), 
    path('edit/<int:cliente_id>/', views.edit_cliente, name='edit_cliente'), 

]