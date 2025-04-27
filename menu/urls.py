from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('attackers/', views.AttackersView.as_view(), name='attackers'),
    path('defenders/', views.DefendersView.as_view(), name='defenders'),
    path('skates/', views.SkatesView.as_view(), name='skates'),
    path('clubs/', views.ClubsView.as_view(), name='clubs'),
]