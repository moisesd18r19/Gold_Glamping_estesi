from . import views
from django.urls import path

urlpatterns = [      
    path('', views.servicios, name='servicios'),
    path('servicio_status_/<int:servicio_id>/', views.change_status_servicio, name='servicio_status'),
    path('create/', views.create_servicio, name='create_servicios'),  
    path('detail/<int:servicio_id>/', views.detail_servicio, name='detail_servicio'), 
    path('delete/<int:servicio_id>/', views.delete_servicio, name='delete_servicio'),
    path('edit/<int:servicio_id>/', views.edit_servicio, name='edit_servicio'),  
]