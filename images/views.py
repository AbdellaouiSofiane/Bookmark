import redis

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from common.decorators import ajax_required

from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action


@login_required
def image_create(request):
	if request.method == 'POST':
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			image = form.save(commit=False)
			image.user = request.user
			image.save()
			create_action(request.user, 'bookmarked image', image)
			return redirect(image)
	else:
		form = ImageCreateForm(data=request.GET)
	return render(request, 
				  'images/image/create.html', 
				  {'form': form})


def image_detail(request, id, slug):
	image = get_object_or_404(Image, id=id, slug=slug)
	r = redis.Redis(host=settings.REDIS_HOST, 
					port=settings.REDIS_PORT, 
					db=settings.REDIS_DB)
	total_views = r.incr(f'image:{image.id}:views')
	return render(request, 
				  'images/image/detail.html',
				  {'image': image,
				   'total_views': total_views})

@login_required
@require_POST
@ajax_required
def image_like(request):
	image_id = request.POST.get('id')
	if image_id :
		try:
			image = Image.objects.get(id=image_id)
		except Image.ObjectDoesNotExist:
			 return JsonResponse({'status': 'failed'})
		else:
			if request.user in image.users_like.all():
				image.users_like.remove(request.user)
			else :
				image.users_like.add(request.user)
				create_action(request.user, 'likes', image)
			return JsonResponse({'total_likes': image.users_like.count() })
	else:
		return JsonResponse({'status': 'failed'})


@login_required
def image_list(request):
	images = Image.objects.all()
	paginator = Paginator(images, 10)
	page_number = request.GET.get('page')
	try:
		images = paginator.page(page_number)
	except PageNotAnInteger:
		images = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		images = paginator.page(paginator.num_pages)
	if request.is_ajax():
		return render(request, 'images/image/list_ajax.html',
							   {'images':images})
	
	return render(request, 'images/image/list.html', 
						  	   {'images':images})