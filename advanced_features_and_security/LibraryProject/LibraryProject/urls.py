from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),

    # Relationship app routes
    path('relationship_app/', include('relationship_app.urls', namespace='relationship_app')),

    # Bookshelf app routes
    path('bookshelf/', include('bookshelf.urls')),
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
