from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home , about


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view( template_name='Login.html')),
    path('about/',about,name='about'),
]