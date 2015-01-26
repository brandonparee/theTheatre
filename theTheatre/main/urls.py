from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^$', 'main.views.about', name='about'),
    url(r'^$', 'main.views.performances', name='performances'),
    url(r'^$', 'main.views.merch', name='merch'),
    url(r'^$', 'main.views.sales', name='sales'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)