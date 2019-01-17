from django.contrib import admin
from django.urls import path, include
from accueil import views as Accueil
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Accueil.home),
    path('accueil/', include('accueil.urls')),
    path('contact/', include('contact.urls')),
    path('inscription/', include('inscription.urls')),
    path('blog/', include('blog.urls')),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
