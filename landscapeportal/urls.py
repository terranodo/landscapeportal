from django.conf.urls import patterns, url, include
from geonode.contrib.geosites.urls import urlpatterns, handler403

urlpatterns = urlpatterns + patterns('',
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^blog-comments/', include('django_comments.urls')),
) 