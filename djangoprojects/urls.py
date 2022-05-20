from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('auth/', include('djoser.urls')),
    path('api/', include('KyvorPipeline.urls')),
    
]


urlpatterns +=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)