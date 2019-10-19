from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import PollForm
from webapp.models import Poll


class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'Poll/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 2


class PollView(DetailView):
    pk_url_kwarg = 'pk'
    model = Poll
    template_name = 'Poll/poll.html'
    context_object_name = 'poll'


class PollCreate(CreateView):
    model = Poll
    template_name = 'Poll/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdate(UpdateView):
    form_class = PollForm
    template_name = 'Poll/update.html'
    model = Poll
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})