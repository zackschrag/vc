from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def messages_home(request):
	return render(request, 'vc_messages.html')

