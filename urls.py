import os
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from bookmarks.views import *

site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
# Examples:
# url(r'^$', 'django_bookmarks.views.home', name='home'),
# url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
# url(r'^admin/', include(admin.site.urls)),

    # Browsing 
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),

    # Session Management
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$',
        TemplateView.as_view(template_name='registration/register_success.html')),

    # Account Management
    (r'^save/$', bookmark_save_page),

    # Site media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': site_media}),

)
