from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #Create a user
        if form.is_valid():
            #save user to database
            user = form.save()
            #log in user
            login(request, user)
            return redirect('/') #/means 'home'

    else:
        #leave blank
        form = UserCreationForm()
    return render(request,
        'accounts/register.html', {'user_create_form': form})
