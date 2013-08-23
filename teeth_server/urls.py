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
  
  # auth
  url(r'^accounts/signin/$', 'teeth_server.views.signin'),
  url(r'^accounts/login/$', 'teeth_server.views.login'),
  
  # main & friend
  url(r'^main/$', 'teeth_server.views.main'),
  url(r'^get_new_target/$', 'teeth_server.views.get_new_target'),
  url(r'^add_friend/$', 'teeth_server.views.add_friend'),
  url(r'^view_my_friend/$', 'teeth_server.views.view_my_friend'),
  
  url(r'^view_friend_req/$', 'teeth_server.views.view_friend_req'),

  # meeting
  url(r'^view_meeting_req/$', 'teeth_server.views.view_meeting_req'),
  url(r'^pick_candidate/$', 'teeth_server.views.pick_candidate'),
  url(r'^deny_req/$', 'teeth_server.views.deny_req'),
  url(r'^accept_req/$', 'teeth_server.views.accept_req'),

  # function
  url(r'^new_cycle/$', 'teeth_server.views.new_cycle'),
  url(r'^sync_friend/$', 'teeth_server.views.sync_friend'),


  # url(r'^invite/$', views.invite, name='invite'),
    
  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
  url(r'^admin_tools/', include('admin_tools.urls')),
)

urlpatterns += static('apidoc/', document_root="docs/_build/html/") + staticfiles_urlpatterns()
