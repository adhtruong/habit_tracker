from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Run

class UsersRunListView(LoginRequiredMixin, ListView):
    model = Run
    template_name = 'tracker/user_runs.html'
    context_object_name = 'runs'

    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return Run.objects.filter(author=user).order_by('-date_posted')

        return Run.objects.filter(author=self.request.user).order_by('-date_ran')



class RunDetailView(DetailView):
    model = Run

class RunCreateView(LoginRequiredMixin, CreateView):
    model = Run
    fields = ['date_ran', 'time', 'distance', 'units', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RunUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Run
    fields = ['date_ran', 'time', 'distance', 'units', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user != post.author:
            return False
        return True

class RunDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Run
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user != post.author:
            return False
        return True
