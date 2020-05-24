
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    

    path('admin/', admin.site.urls),
    path('products/', include('product.urls', namespace='products')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', views.home)
    ]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)