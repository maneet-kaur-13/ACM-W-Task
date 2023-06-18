from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
#from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import Food


def home(request):
    #return render(request, 'users/home.html')
    foods = Food.objects.all()
    return render(request, 'users/home.html', {'foods': foods})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
   return render(request,'users/profile.html')
#def profile(request):
    #user_profile = request.user.userprofile
    #form = UserProfileForm(instance=user_profile)

    #if request.method == 'POST':
        #form = UserProfileForm(request.POST, instance=user_profile)
        #if form.is_valid():
            #form.save()
            #return redirect('profile')

    #return render(request, 'profile.html', {'form': form})



