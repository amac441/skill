from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^dashboard/', TemplateView.as_view(template_name="pages/main.html"), name='dash'),


    #url(r'^$', ListView.as_view(
    #                        queryset=Portfolio.objects.all().   #add the filter later!
    #                        order_by("-created")[:2],  #need to change to rank
    #                        context_object_name = "portfolio",
    #                        template_name="index.html")),
)