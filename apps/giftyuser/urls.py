from django.conf.urls import patterns, include, url

from apps.giftyuser import views

# URLS
urlpatterns = patterns('',
    
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^user/create/$', views.UserCreate.as_view(), name='signup'),

)