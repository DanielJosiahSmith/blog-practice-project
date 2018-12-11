from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm

def index(request):
	"""The home page for Blog"""
	return render(request, 'blogs/index.html')
	
def post(request):
	"""Where user can add a new topic"""
	topics = Topic.objects.order_by('date_added')
	
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data.
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post'))
		
	context = {'topics': topics, 'form': form}
	return render(request, 'blogs/post.html', context)
	
	
	
