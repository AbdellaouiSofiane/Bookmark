from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out

from .models import Profile


@receiver(user_logged_out)
def user_last_logout(sender, request, user, **kwargs):

	user.profile.last_logout = timezone.now()
	user.profile.save()
	
