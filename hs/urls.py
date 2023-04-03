from django.contrib import admin
from django.conf import settings
from django.urls import path, include # Import 'include'
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.home.urls")),
    path('chat/', include("apps.chat.urls")),
    path('appointment', include("apps.appointment.urls")),
    path('news/', include('apps.news.urls')),  # News
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
