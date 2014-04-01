from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/$', 'moviedatabase.views.listall'),
    url(r'^movies/(?P<movie_id>\d+)/$', 'moviedatabase.views.detail'),
    url(r'^Norskkurs/index', 'Norskkurs.views.index'),
    url(r'^Norskkurs/newelev', 'Norskkurs.views.newelev'),
    url(r'^Norskkurs/listall', 'Norskkurs.views.listall'),
    url(r'^Norskkurs/(?P<customer_id>\d+)', 'Norskkurs.views.detail'),
    url(r'^Norskkurs/fravar', 'Norskkurs.views.fravar'),
    url(r'^Norskkurs/registrerfravar', 'Norskkurs.views.registrerfravar'),
    url(r'^Norskkurs/visfravar', 'Norskkurs.views.visfravar'),
    url(r'^Norskkurs/adminkurs', 'Norskkurs.views.adminkurs'),
    url(r'^Norskkurs/adminlarer', 'Norskkurs.views.adminlarer'),
    url(r'^Norskkurs/search', 'Norskkurs.views.search')

)
