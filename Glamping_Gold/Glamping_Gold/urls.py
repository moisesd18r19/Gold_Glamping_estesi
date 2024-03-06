
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Pdfview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('tipocabañas/', include('tipocabañas.urls')), 
    path('clientes/', include('cliente.urls')),
    path('servicios/', include('servicios.urls')),
    path('cabañas/' , include('cabañas.urls')),
    path('reservas/', include('reservas.urls')),    
    path('pagos/', include('pagos.urls')),
    path('login/', views.login, name='login'),
    path('', views.landing, name='landing'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('Pdfview/<int:pk>/', Pdfview.as_view(), name='Pdfview'),
    
    

    
  
    
]
