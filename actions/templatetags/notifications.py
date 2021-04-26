from django import template
from ..models import Action


register = template.Library()


@register.inclusion_tag('actions/action/detail.html')
def show_notifications(request):
	actions = Action.objects.exclude(user=request.user)
	following_ids = request.user.following.values_list('id',
										   flat=True)
	if following_ids:
		actions = actions.filter(user_id__in=following_ids)
	actions = actions.select_related('user', 'user__profile')\
					 .prefetch_related('target')[:10]
	return {'actions': actions}



@register.simple_tag
def notification_number(request):
	actions = Action.objects.exclude(user=request.user)
	following_ids = request.user.following.values_list('id',
										   flat=True)
	if following_ids:
		actions = actions.filter(user_id__in=following_ids)
	if request.user.profile.last_logout:
		actions = actions.filter(created__gte=request.user.profile.last_logout)
	
	return actions.count()