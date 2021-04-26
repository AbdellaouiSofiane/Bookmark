from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('actions.urls', namespace='actions')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('images/', include('images.urls', namespace='images')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, 
						  document_root=settings.MEDIA_ROOT)