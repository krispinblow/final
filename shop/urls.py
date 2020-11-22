<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
=======
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
>>>>>>> cee217ef8247483092a4e186f2cbb868d393e645
                          document_root=settings.MEDIA_ROOT)