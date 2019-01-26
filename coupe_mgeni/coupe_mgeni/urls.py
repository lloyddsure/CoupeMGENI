from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from accueil import views as Accueil
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', Accueil.home),
    url(r'^admin', admin.site.urls),
    url(r'^accueil', include('accueil.urls')),
    path(r'contact', include('contact.urls')),
    path(r'inscription', include('inscription.urls')),
    path(r'blog', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
#urlpatterns +=
#urlpatterns +=
