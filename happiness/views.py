from django.views import generic

from happiness.forms import HappinessForm
from happiness.models import Happiness

class ListHappinessView(generic.ListView):
    template_name = 'happiness/list_happiness.html'
    context_object_name = 'happiness_list'
    pagination_by = 10

    def get_queryset(self):
        return Happiness.objects.filter(user=self.request.user)


class CreateHappiness(generic.CreateView):
    template_name = 'happiness/happiness_form.html'
    form_class = HappinessForm
    success_url = '/account'