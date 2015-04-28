from django.forms import ModelForm


from apps.giftyuser.models import User





class UserForm(ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'address', 'phone', 'password']