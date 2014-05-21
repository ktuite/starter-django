from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_base.views.home', name='home'),
    url(r'^', include('custom_app.urls')),


    # account mumbo-jumbo [Views automatically set up by Django]
    url(r'^login-form/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^accounts/password/reset/$','django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password/reset/done/'}, name="password_reset"),
    url(r'^accounts/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/password/done/$','django.contrib.auth.views.password_reset_complete'),


    # more account mumbo-jumbo [Views that should be customized]
    url(r'^accounts/profile/edit/$', 'django_base.account_views.edit_profile', name='edit_profile'),
    url(r'^accounts/profile/$', 'django_base.account_views.profile', name='profile'),
    url(r'^accounts/register/$', 'django_base.account_views.register', name='register'),


    url(r'^admin/', include(admin.site.urls)),
)
