from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext as _

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = _('Application Name')
admin.site.site_title = _('Application Name')
admin.site.index_title = _('Application Name')
