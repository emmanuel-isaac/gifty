# Django default modules
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext


# Local modules
from apps.giftyuser.models import User, StaffMember
from apps.giftyuser.serializers import UserSerializer, StaffMemberSerializer
from apps.giftyuser.forms import UserForm, LoginForm


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
		form = LoginForm()
		return render_to_response('giftyuser/login.html', locals(), context_instance=RequestContext(request))

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid:
			username = form.data['username']
			password = form.data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('home'), locals())
		return render_to_response('giftyuser/login.html', locals(), context_instance=RequestContext(request))


# Class Based Logout View
class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('home'), locals())

# Class Based Signup View
class UserCreate(View):
	def get(self, request):
		form = UserForm()
		return render_to_response('auth/signup.html', locals(), context_instance=RequestContext(request))

	def post(self, request):
		form = UserForm(request.POST)
		if form.is_valid():
			if request.POST.get('password') == request.POST.get('confirm-password'):
				try:
					new_user = form.save(commit=False)
					new_user.set_password(request.POST.get('password', ''))
					new_user.save()
					user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
					login(request, user)
					return HttpResponse('Signed in and Logged in')

				except Exception, e:
					raise e
			else:
				password_error = 'Passwords do not match'
				return render_to_response('auth/signup.html', locals(), context_instance=RequestContext(request))
		password_error = 'Please, fill all fields'
			
		return render_to_response('auth/signup.html', locals(), context_instance=RequestContext(request))










