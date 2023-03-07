from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('show_book.urls')),
    path('', include('parser_py.urls')),
    path('', include('custom_user.urls')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)