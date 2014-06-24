from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from velocichapter.forms import LoginForm

def main_page(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect('/messages/')

            else:
                return render(request, 'registration/login.html', { 'form': { 'errors': 'There was an error in authentication. Please try again.' }})
    else:
        return render(request, 'registration/login.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')