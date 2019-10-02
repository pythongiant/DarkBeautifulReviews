from django.shortcuts import render
from django.views.generic.base import TemplateView
from news.models import News

class HomeView(TemplateView):
    template_name = "home/index.html"
