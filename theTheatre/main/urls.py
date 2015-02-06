from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^about/', 'main.views.about', name='about'),
    url(r'^performances/$', 'main.views.performances', name='performances'),
    url(r'^performances/(?P<id_num>\w{0,50})/$', 'main.views.performances_unit', name='performances_unit'),
    url(r'^merch/$', 'main.views.merch', name='merch'),
    url(r'^merch/(?P<id_num>\w{0,50})/$', 'main.views.merch_unit', name='merch_unit'),
    url(r'^sales/', 'main.views.sales', name='sales'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)