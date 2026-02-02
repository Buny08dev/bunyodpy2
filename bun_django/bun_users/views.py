from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.views.generic import FormView,ListView,View,DetailView,TemplateView,DeleteView,UpdateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy

# Create your views here.

class Registeview(TemplateView):
    template_name='login.html'