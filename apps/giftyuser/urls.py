from django.conf.urls import patterns, include, url

from apps.giftyuser import views

# URLS
urlpatterns = patterns('',
    
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.UserCreate.as_view(), name='signup'),
    url(r'^(?P<activation_key>\w+)/activate/', views.register_confirm, name='register_confirm'),

)