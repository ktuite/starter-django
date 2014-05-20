from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'custom_app.views.index', name='index'),


    url(r'^simple_view$', 'custom_app.views.simple_view'), # really simple view that doesnt use any templates or static files
)