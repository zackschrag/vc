from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from vc_auth.forms import UserForm, ChapterForm

def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()            
			user.set_password(user.password)
			user.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# invalid forms
		else:
			print user_form.errors
	
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()

	# Render the template depending on the context.
	return render(request, 'register.html', {'user_form': user_form, 'registered': registered})

def register_chapter(request):

	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		chapter_form = ChapterForm(data=request.POST)

		if chapter_form.is_valid():
			# Save the user's form data to the database.
			chapter = chapter_form.save()            
			chapter.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# invalid forms
		else:
			print chapter_form.errors
	
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		chapter_form = ChapterForm()

	return render(request, 'register_chapter.html', {'chapter_form': chapter_form, 'registered': registered})
