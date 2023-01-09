from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View

class Sira(View):
    template_name = 'sira.html'