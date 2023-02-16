from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for {username}! Now you can login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    
    context = {
        'form' : form,
        'title' : 'register'
    }
    
    return render(request, "users/register.html", context=context)

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Profile successfully updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form': p_form,
        'u_form': u_form,
    }
    return render(request, "users/profile.html", context=context)