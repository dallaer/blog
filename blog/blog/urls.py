from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('twit.urls')),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)