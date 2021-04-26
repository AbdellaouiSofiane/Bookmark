from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = get_user_model()
		fields = ('username', 'email')


class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth', 'gender', 'photo')


class UserEditForm(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields = ('first_name', 'last_name', 'email')