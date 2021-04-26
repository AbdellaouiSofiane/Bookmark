from django.shortcuts import render

from actions.models import Action

def dashboard(request):
	return render(request, 'actions/dashboard.html')
	