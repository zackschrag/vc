from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from vc.forms import UserForm, ChapterForm
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html')

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		chapter_form = ChapterForm(data=request.POST)

		if user_form.is_valid() and chapter_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()
			chapter = chapter_form.save()

			user.set_password(user.password)
			user.save()

			# Update our variable to tell the template registration was successful.
			registered = True
			return redirect('vc.views.home')
		# invalid forms
		else:
			print user_form.errors
	
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		chapter_form = ChapterForm()

	# Render the template depending on the context.
	return render(request, 'register.html', {'user_form': user_form, 'chapter_form': chapter_form, 'registered': registered})

def login(request):
	return render(request, 'login.html')

@login_required
def home(request):
	return render(request, 'home.html')