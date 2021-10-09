from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.views.generic import TemplateView
from machina import urls as machina_urls

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('test', views.test, name='test'),
    path('vvod', views.vvod, name='vvod'),
    path('notes', views.notes, name='notes'),
    path('user', views.user, name='user'),
    path('grappelli/', include('grappelli.urls')),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('user_login', views.user_login, name='user_login'),
    path('login', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('str', views.str, name='str'),
    path('accounts/', include('allauth.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('forum/', include(machina_urls)),
]


