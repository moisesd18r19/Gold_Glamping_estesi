from . import views
from django.urls import path

urlpatterns = [      
    path('', views.tipocabañas, name='tipocabañas'),
    path('tipocabaña_status_/<int:tipocabaña_id>/', views.change_status_tipocabaña, name='tipocabaña_status'), 
    path('create/', views.create_tipocabaña, name='create_tipocabaña'), 
    path('', views.tipocabañas, name='tipocabañas'), 
    path('detail/<int:tipocabaña_id>/', views.detail_tipocabaña, name='detail_tipocabaña'),
    path('delete/<int:tipocabaña_id>/', views.delete_tipocabaña, name='delete_tipocabaña'),  
    path('edit/<int:tipocabaña_id>/', views.edit_tipocabaña, name='edit_tipocabaña'),  
    
    # path("lista_tipocabaña/", views.lista_tipocabaña.as_view(), name="lista_tipocabaña")
]
         
         
