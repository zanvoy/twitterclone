from django.shortcuts import render, reverse, HttpResponseRedirect 
from django.contrib.auth import login, logout, authenticate
from authentication.forms import LoginForm

def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    html = 'base_form.html'
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))