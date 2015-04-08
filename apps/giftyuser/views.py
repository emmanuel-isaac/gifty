# Django default modules
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Local modules
from apps.giftyuser.models import User, StaffMember
from apps.giftyuser.serializers import UserSerializer, StaffMemberSerializer


# Third party modules
from rest_framework import viewsets

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StaffMemberViewSet(viewsets.ModelViewSet):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer

# Class Based Login View
class LoginView(View):
	def get(self, request):
		return HttpResponseRedirect(reverse('home'), locals())

	def post(self, request):
		print request.POST
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		if username and password:
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print request.user.is_authenticated()
				return HttpResponseRedirect(reverse('home'), locals())
			else:
				print "nay"
				
		else:
			return HttpResponseRedirect(reverse('home'), locals())

		return HttpResponse("This is the login view")



# Class Based Logout View
class LogoutView(View):
	def get(self, request):
		print request
		logout(request)
		return render_to_response('auth/user_logout.html', locals())


class UserCreate(CreateView):
	model = User
	fields = ['first_name', 'last_name', 'username', 'email', 'address', 'phone', 'password',]
	template_name = 'auth/signup.html'











