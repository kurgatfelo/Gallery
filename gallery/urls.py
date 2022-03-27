from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.homepage,name='home'),
    re_path(r'^search/', views.search_category, name='search_category'),
    re_path(r'^location/(?P<location_name>\w+)',views.get_image_location,name = 'location'),
    re_path('^image/(?P<image_id>\d+)/$',views.image_properties, name='image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)