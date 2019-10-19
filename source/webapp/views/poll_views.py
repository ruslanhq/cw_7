from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from webapp.forms import PollForm
from webapp.models import Poll, Choice, Answer


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


class PollDelete(DeleteView):
    template_name = 'Poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')


class MainPollView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choices = poll.choices.all()
        print(choices)
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'Main_Poll.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['answers']
        answers = get_object_or_404(Choice, pk=pk)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(answers=answers, poll=poll)
        return redirect('index')

