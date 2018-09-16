from  django.contrib import admin
from django.contrib import path, include

urlpatterns = [
    path('admin/', admin.site.urls) 
    path('', include('cliente.urls'))
]       