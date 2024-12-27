from .models import CreateForum
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'forums/index.html'
    context_object_name = 'latest_forum_list'

    def get_queryset(self):
        return CreateForum.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = CreateForum
    template_name = 'forums/detail.html'

    def get_queryset(self):
        return CreateForum.objects.filter(pub_date__lte=timezone.now())



