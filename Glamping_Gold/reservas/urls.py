from .import views
from django.urls import path


urlpatterns = [      
    path('', views.reservas, name='reservas'),
	# path('reserva_status_/<int:reserva_id>/', views.change_status_reserva, name='reserva_status'),  
    path('create/', views.create_reserva, name='create_reserva'),
    path('detail/<int:reserva_id>/', views.detail_reserva, name='detail_reserva'),  
    path('delete/<int:reserva_id>/', views.delete_reserva, name='delete_reserva'),           
]