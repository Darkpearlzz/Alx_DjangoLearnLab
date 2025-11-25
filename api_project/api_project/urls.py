from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # API endpoints under /api/
    # optional: path('', include('api.urls')) to expose at root
]
