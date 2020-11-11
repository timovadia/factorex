# encoding: utf-8
from django.conf.urls import patterns, include, url
from exchange.views import *
from django.contrib import admin
from django.views.generic import TemplateView
from accounts.views import *
from feedback.views import FeedbackCreate
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'factorex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Browsing
    # url(r'^$', index),
    url(r'^$', land_page),
    url(r'^user/(?P<id>\w+)/$', user_page),
    url(r'^profile/', profile),
    url(r'^account/(?P<id>\w+)/$', account_page),
    url(r'^contact/$', FeedbackCreate.as_view(), name='request_contact'),
    url(r'^contact/success/$', TemplateView.as_view(template_name="contact_success.html")),
    url(r'^request-invite/$', InviteCreate.as_view(), name='request_invite'),
    url(r'^request-invite/success/$', invite_success),

    # Session management
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register_page),
    url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)