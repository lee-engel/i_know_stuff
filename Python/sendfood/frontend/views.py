from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .models import User, MenuItem


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(ListView):
    template_name = 'menu.html'
    model = MenuItem


class CartView(TemplateView):
    template_name = 'cart.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


