from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'teeth_server.views.home', name='home'),
	url(r'^hello/$', 'teeth_server.views.home'),
	url(r'^search-form/$', 'teeth_server.views.search_form'),
	url(r'^search/$', 'teeth_server.views.search'),
	url(r'^accounts/login/$', 'teeth_server.views.login'),
	#url(r'^accounts/logout/$', 'teeth_server.views.logout'),
	url(r'^accounts/example/$', 'teeth_server.views.example'),
    url(r'^main/$', 'teeth_server.views.main'),
	url(r'^open/$', 'teeth_server.views.open'),
	# url(r'^invite/$', views.invite, name='invite'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
