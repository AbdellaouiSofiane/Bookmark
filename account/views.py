from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import JsonResponse

from common.decorators import ajax_required

from .forms import UserRegisterForm, ProfileEditForm, UserEditForm
from .models import Profile, Contact
from actions.utils import create_action


def register(request):
	if request.method == 'POST' :
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			Profile.objects.create(user=new_user)
			create_action(new_user, 'has created an account')
			messages.success(request, 'Your account has successfully been created.')
			return redirect('account:login')
	else:
		form = UserRegisterForm()
	return render(request, 'account/register.html', {'form': form})


@login_required
def edit_profile(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, 
								 data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
									   data=request.POST,
									   files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your account has successfully been updated.')
		else :
			messages.danger(request, 'Please correct the errors below')
	else : 
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'account/edit.html', 
						   {'user_form': user_form,
						    'profile_form': profile_form})



@login_required
def profile(request):
	return render(request, 'account/profile.html')


@login_required
def user_list(request):
	users = get_user_model().objects.all()
	return render(request, 'user/list.html',
		{'users': users})


@login_required
def user_detail(request, username):
	user = get_object_or_404(get_user_model(),
					username=username,
					is_active=True)
	if user == request.user :
		return redirect('account:profile')
	else:
		return render(request,
			      'user/detail.html',
				  {'user': user})


@login_required
@require_POST
@ajax_required
def user_follow(request):
	User = get_user_model()
	user_id = request.POST.get('id')
	if user_id :
		try :
			user = User.objects.get(id=user_id)
			if user in request.user.following.all():
				Contact.objects.filter(user_from=request.user,
									   user_to=user).delete()
			else:
				Contact.objects.get_or_create(
									user_from=request.user,
									user_to=user)
				create_action(request.user, 'is following', user)
			return JsonResponse({'status':'ok'})
		except User.DoesNotExist:
			return JsonResponse({'status':'error'})
	return JsonResponse({'status':'error'})


