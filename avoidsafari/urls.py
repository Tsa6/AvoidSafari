from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^info$', TemplateView.as_view(template_name="info.html")),
    url(r'^$', views.MainView.as_view()),
]
