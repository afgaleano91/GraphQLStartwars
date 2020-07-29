from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView


class PrivateView(LoginRequiredMixin, GraphQLView):
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'