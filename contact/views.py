from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from .models import Message
from .forms import MessageForm


class MessageDetailView(DetailView):
    model = Message


class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()