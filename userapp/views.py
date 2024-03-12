from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)
