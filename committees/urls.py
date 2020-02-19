from django.urls import path

from . import views

app_name = 'committees'
urlpatterns = [
    path('', views.IndexView.as_view(), name='committees'),
    path('<slug:slug>/', views.DetailView.as_view(), name='committee_detail'),
]
