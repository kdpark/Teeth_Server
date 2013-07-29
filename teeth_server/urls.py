from django.conf.urls import patterns, include, url
from teeth_server.views import home, current_datetime, hour_ahead
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'teeth_server.views.home', name='home'),
	url(r'^hello/$', home),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d+)/$', hour_ahead),
    # url(r'^teeth_server/', include('teeth_server.foo.urls')),
	
	# url(r'^invite/$', views.invite, name='invite'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
