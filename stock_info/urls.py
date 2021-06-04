from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:stock_name>/', views.stock_info, name = "stock_info"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)