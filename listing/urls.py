from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listing, name = "listing"),
    path('stock_info/', include('stock_info.urls'))
]
