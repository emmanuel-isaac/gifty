from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin



from apps.giftyuser.models import User, StaffMember
from apps.giftyuser.views import (
	UserViewSet,
	StaffMemberViewSet,
	LoginView,
	LogoutView,
    UserCreate,
)
from apps.gift.views import GiftItemViewSet, GiftPackViewSet, HomeView
from apps.cart.views import CartViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'staff', StaffMemberViewSet)
router.register(r'items', GiftItemViewSet)
router.register(r'packs', GiftPackViewSet)
router.register(r'carts', CartViewSet)


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^user/create/$', UserCreate.as_view(), name='signup'),
)
