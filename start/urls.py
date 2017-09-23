# howdy/urls.py
from django.conf.urls import url
from start import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),  # Add this /about/ route
url(r'^form/$', views.FormPageView.as_view()),  # Add this /about/ route
]
