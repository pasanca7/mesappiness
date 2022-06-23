from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView

from mesappiness.settings import LANGUAGE_CODE
from .forms import UserRegisterForm
from django.utils.translation import gettext_lazy as _

class Index(TemplateView):
    template_name = 'account/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = _(self.request.user.username)
        context['language_code'] = LANGUAGE_CODE
        return context

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