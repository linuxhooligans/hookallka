from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from hookallka.forms import CustomUserCreationForm
import logging

logger = logging.getLogger(__name__)


@login_required
def home(request):
    return render(request, "registration/success.html", {})


def contact(request):
    return render(request, "registration/contact.html", {})


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
