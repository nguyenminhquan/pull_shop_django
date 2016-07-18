from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_id>[0-9]+)/$', views.cat_detail, name='cat_detail'),
    url(r'^[0-9]+/(?P<product_id>[0-9]+)/$', views.pro_detail, name='pro_detail'),
]
