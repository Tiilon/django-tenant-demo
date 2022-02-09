from django.views.generic import ListView
from .models import Sweet
from django.shortcuts import render


class Index(ListView):
    model = Sweet
    template_name = 'sweet_tenant/index.html'
    context_object_name = 'sweets'
