from .import views
from django.urls import path


urlpatterns = [      
    path('', views.reservas, name='reservas'),
    path('create/', views.create_reserva, name='create_reserva'),
    path('detail/<int:reserva_id>/', views.detail_reserva, name='detail_reserva'),  
    path('cancel/<int:reserva_id>/', views.cancel_reserva, name='cancel_reserva'),           
    path('edit/<int:reserva_id>/', views.edit_reserva, name='edit_reserva'),          
]