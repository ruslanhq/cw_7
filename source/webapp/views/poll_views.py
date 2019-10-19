from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Poll


class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'Poll/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 2