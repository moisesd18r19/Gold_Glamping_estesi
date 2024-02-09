from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cabañas, name='cabañas'),
	path('cabaña_status_/<int:cabaña_id>/', views.change_status_cabaña, name='cabaña_status'),      
    path('create/', views.create_cabaña, name='create_cabaña'),
    path('detail/<int:cabaña_id>/', views.detail_cabaña, name='detail_cabaña'), 
    path('delete/<int:cabaña_id>/', views.delete_cabaña, name='delete_cabaña'),      
    path('edit/<int:cabaña_id>/',views.edit_cabaña, name='edit_cabaña')
    
  
]