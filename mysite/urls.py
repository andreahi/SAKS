from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^exports/', include('data_exports.urls', namespace='data_exports')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Norskkurs/loggut$', 'Norskkurs.views.logout_view'),
    url(r'^Norskkurs/index$', 'Norskkurs.views.index'),
    url(r'^Norskkurs/newelev$', 'Norskkurs.views.newelev'),
    url(r'^Norskkurs/listall$', 'Norskkurs.views.listall'),
    url(r'^Norskkurs/(?P<elev_id>\d+)/$', 'Norskkurs.views.detail',name='detail'),
    url(r'^Norskkurs/fravar$', 'Norskkurs.views.fravar'),
    url(r'^Norskkurs/registrerfravar$', 'Norskkurs.views.registrerfravar'),
    url(r'^Norskkurs/visfravar$', 'Norskkurs.views.visfravar'),
    url(r'^Norskkurs/adminkurs$', 'Norskkurs.views.adminkurs'),
    url(r'^Norskkurs/adminlarer$', 'Norskkurs.views.adminlarer'),
    url(r'^Norskkurs/search$', 'Norskkurs.views.search'),
    url(r'^Norskkurs/startkurs$', 'Norskkurs.views.startkurs'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^Norskkurs/listallekurs$', 'Norskkurs.views.listallekurs'),
    url(r'^Norskkurs/instillinger$', 'Norskkurs.views.instillinger'),
    url(r'^Norskkurs/sok$', 'Norskkurs.views.sok'),
    url(r'^Norskkurs/statsborgerskap$', 'Norskkurs.views.statsborgerskap'),
    url(r'^Norskkurs/nyttvedtak$', 'Norskkurs.views.nyttvedtak'),
    url(r'^Norskkurs/opphold', 'Norskkurs.views.opphold')
)
