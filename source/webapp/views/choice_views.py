from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreatePoll(CreateView):
    template_name = 'Choice/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)


class ChoiceCreate(CreateView):
    model = Choice
    template_name = 'Choice/create.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})

