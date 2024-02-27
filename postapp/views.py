from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView

class HomePost(ListView):
    model = Post
    template_name = 'home.html'