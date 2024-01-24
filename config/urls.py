from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1', ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shop/categories/', include('shop_app.urls.category_urls')),
    path('api/shop/products/', include('shop_app.urls.product_urls')),
    path('api/banners/', include('banner_app.urls')),
    path('api/home/', include('shop_app.url')),
    path('api/user/', include('user_app.urls')),
    path('api/sellers/', include('user_app.seller.urls')),
    path('api/orders/', include('shop_app.urls.order_urls')),
    path('api/regions/', include('location_app.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
