from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from root.settings import MEDIA_URL, MEDIA_ROOT
urlpatterns = [
    path('foods/', include('apps.foods.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('apps.orders.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
