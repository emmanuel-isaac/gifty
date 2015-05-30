# Django default modules
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.mail import send_mail

# Python modules
import hashlib, datetime, random

# Local modules
from apps.giftyuser.models import User
from apps.giftyuser.serializers import UserSerializer
from apps.giftyuser.forms import UserForm, LoginForm
from services.utilities import send_django_mail


# Third party modules
from rest_framework import viewsets

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.set_password(form.data['password'])
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            new_user.activation_key = hashlib.sha1(salt+new_user.email).hexdigest()
            new_user.save()
            body = "<html>\
                        Click on this <a href='%s/user/%s/activate/'>link</a> to activate your account\
                    </html>" % (request.META['HTTP_ORIGIN'], new_user.activation_key)
            send_django_mail('MarbalNG Account Confirmation', 'isaac.e.ayodeji@gmail.com', [new_user.email], html_content=body)
            return HttpResponseRedirect(reverse('home'), locals())

        return render_to_response('auth/signup.html', locals(), context_instance=RequestContext(request))

# Function to confirm user account
def register_confirm(request, activation_key):
    if request.user.is_active:
        return HttpResponseRedirect(reverse('home'))
    import ipdb; ipdb.set_trace()
    user = get_object_or_404(User, activation_key=activation_key)
    user.is_active = True
    user.save()
    send_django_mail('Welcome to MarbalNG', 'isaac.e.ayodeji@gmail.com', [user.email], 'Welcome to MarbalNG')
    return HttpResponseRedirect(reverse('login'))










