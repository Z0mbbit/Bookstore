from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    template_name = "signup.html"
    success_url = reverse_lazy("book_list")

    form_class = UserCreationForm