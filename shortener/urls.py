from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.create_short_url, name='shorturl'),
    url(r'^update_url/$', views.update_short_url, name='update'),
    url(r'^[\w]+/$', views.redirect_to_source_url, name='sourceurl'),
 ]