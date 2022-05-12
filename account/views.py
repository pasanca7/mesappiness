from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} created')
            return redirect('index')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)