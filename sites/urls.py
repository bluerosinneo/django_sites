from django.urls import path
from .views import (
    SiteListView,
    SiteDetailView,
    SiteCreateView,
    SiteUpdateView,
    SiteDeleteView,
)

urlpatterns = [
    path("site/<int:pk>/", SiteDetailView.as_view(), name="site_detail"),
    path("site/new/", SiteCreateView.as_view(), name="site_new"),
    path("site/<int:pk>/edit/", SiteUpdateView.as_view(), name="site_edit"),
    path("site/<int:pk>/delete/", SiteDeleteView.as_view(), name="site_delete"),
    path("", SiteListView.as_view(), name="home"),
]
