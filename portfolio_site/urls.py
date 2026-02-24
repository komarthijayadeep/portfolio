from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import portfolio_site.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects_app.urls')),
    path('auth/', include('accounts_app.urls')),
    path('', include('contact_app.urls')),
    path('api/', include('api_app.urls')),  # contact/ is at root level or under /contact/? defined in app urls as 'contact/'
    path('test-404/', portfolio_site.views.custom_404, kwargs={'exception': Exception('Test')}),
]

handler404 = 'portfolio_site.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
