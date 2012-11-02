from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Places app
    url(r'^places/', include('places.urls')),
    # Admin app
    url(r'^admin/', include(admin.site.urls))
)
