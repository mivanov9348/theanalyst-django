from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('',include('core.urls')),
    path('reports/', include('reports.urls')),
    path("players/", include("players.urls")),
]
