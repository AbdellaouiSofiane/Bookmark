from django.urls import path
from . import views

app_name = 'images'


urlpatterns = [
	path('', views.image_list, name='image_list'),
	path('create/', views.image_create, name='image_create'),
	path('<int:id>/<slug:slug>/', views.image_detail, name='image_detail'),
	path('like/', views.image_like, name='image_like'),
]