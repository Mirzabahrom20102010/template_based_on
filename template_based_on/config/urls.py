from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import home_view
from posts import urls

app_name = 'config'

urlpatterns = [
    path('', home_view, name='landing_page'),
    path('admin/', admin.site.urls),
    path('post/', include('posts.urls')),
    path('account/', include('accounts.urls')),
    # path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)