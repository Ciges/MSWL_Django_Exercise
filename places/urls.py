from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('places.views',
    url(r'^$', 'list_places'),
    url(r'^orderbyviews/$', 'list_places_order_by_views'),
    url(r'^(?P<place_id>\d+)/$', 'view_place'),
    url(r'^admin/', include(admin.site.urls))
)
