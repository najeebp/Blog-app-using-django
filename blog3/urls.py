from django.conf.urls import patterns, include, url
from blog3 import views
     
     
urlpatterns = patterns('',
    url(r'^$', views.home, name='view'),
    url(r'login$', views.login_page, name='login_page'),
    url(r'logout$', views.logout_view, name='logout_view'),
    url(r'^signup$', views.Signup_page, name='Signup_page'),
    url(r'^signup/done$', views.Signup_page, name='Signup_values'),
    # # url(r'^logged/$', views.Login_values, name='Login_values'),
    url(r'new_post$', views.post_entry, name='post_entry'),
    url(r'posted$', views.post_entry, name='pos_entry'),
    url(r'delete/(?P<post_id>[0-9]+)/(?P<name>\w+)/$', views.post_delete, name='post_delete'),
    url(r'edit/(?P<post_id>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'read_more/(?P<post_id>[0-9]+)/$', views.read_more, name='read_more'),
    url(r'back_home$', views.back_home, name='back_home'),
    url(r'password_reset$', views.password_reset, name='password_reset'),

    url(r'changing-password/(?P<encrypt_string>[a-zA-Z0-9_=]+)/$', views.reset_password, name='reset_password'),
    # # url(r'^view$', views.view, name='view'),
    )
# url(r'^$', views.Login_page, name='Login_page'),