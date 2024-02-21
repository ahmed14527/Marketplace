from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="-marketplace",
        default_version="v1",
        description="API for marketplace",
        terms_of_service="https://your-terms-of-service-url.com/",
        contact=openapi.Contact(email="ahmed890magdy@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item.urls')),
    path('', include('conversation.urls')),
    path('', include('account.urls')),
    path('', include('resetpassword.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]  
    
    
urlpatterns+=staticfiles_urlpatterns()