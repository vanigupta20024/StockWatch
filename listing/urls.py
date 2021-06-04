from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listing, name = "listing"),
    path('stock_info/', include('stock_info.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)