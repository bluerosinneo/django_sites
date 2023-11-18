from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Site


class SiteListView(ListView):
    model = Site
    template_name = "home.html"


class SiteDetailView(DetailView):
    model = Site
    template_name = "site_detail.html"


class SiteCreateView(CreateView):
    model = Site
    template_name = "site_new.html"
    fields = ["title", "description", "link"]


class SiteUpdateView(UpdateView):
    model = Site
    template_name = "site_edit.html"
    fields = ["title", "description", "link"]


class SiteDeleteView(DeleteView):
    model = Site
    template_name = "site_delete.html"
    success_url = reverse_lazy("home")
