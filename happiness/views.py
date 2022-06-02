from django.views import generic

from happiness.forms import HappinessForm
from happiness.models import Happiness

class ListHappinessView(generic.ListView):
    template_name = 'happiness/list_happiness.html'
    context_object_name = 'happiness_list'
    paginate_by = 5
    model = Happiness

    def get_queryset(self):
        return Happiness.objects.filter(user=self.request.user)


class CreateHappiness(generic.CreateView):
    template_name = 'happiness/happiness_form.html'
    form_class = HappinessForm
    success_url = '/happiness/list'

    def get_initial(self):
        self.initial.update({ 'user': self.request.user })
        return self.initial


class ReadHappiness(generic.DetailView):
    model = Happiness
    template_name = 'happiness/happiness_detail.html'