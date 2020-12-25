from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'users.views.first_page'),
    url(r'^register/','users.views.register'),
    url(r'^user_login/','users.views.user_login'),
    url(r'^user_logout/','users.views.user_logout'),
    url(r'^diff_response/','users.views.diff_response'),
    url(r'^user_only/','users.views.user_only'),
    url(r'^specific_user/','users.views.specific_user'),
)