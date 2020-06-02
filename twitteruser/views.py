from django.shortcuts import render, reverse, HttpResponseRedirect 
from twitteruser.forms import RegesterForm
from twitteruser.models import SomeUser

def regesterview(request):
    if request.method == 'POST':
        form = RegesterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newUser = SomeUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
        newUser.save()
    form = RegesterForm()
    html = 'regester.html'
    return render(request, html, {'form': form})