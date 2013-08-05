from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'teeth_server.views.home', name='home'),
	url(r'^hello/$', 'teeth_server.views.home'),
	url(r'^search-form/$', 'teeth_server.views.search_form'),
	url(r'^accounts/signin/$', 'teeth_server.views.signin'),
	url(r'^accounts/login/$', 'teeth_server.views.login'),
	url(r'^accounts/example/$', 'teeth_server.views.example'),
    url(r'^main/$', 'teeth_server.views.main'),
	url(r'^open/$', 'teeth_server.views.open'),
	
	# url(r'^invite/$', views.invite, name='invite'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static('apidoc/', document_root="docs/_build/html/") + staticfiles_urlpatterns()
