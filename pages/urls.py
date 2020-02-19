from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('volmun-101/', views.VolMUN101View.as_view(), name='volmun-101'),
    path('delegate-guidebook/', views.DelegateGuidebookView.as_view(), name='delegate-guidebook'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('conference-handbook/', views.ConferenceHandbookView.as_view(), name='conference-handbook'),
    path('advisor-guidebook/', views.AdvisorGuidebookView.as_view(), name='advisor-guidebook'),
    path('fees-and-accommodations/', views.FeesAndAccommodationsView.as_view(), name='fees-and-accommodations'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('secretariat/', views.SecretariatView.as_view(), name='secretariat'),
    path('digital-press-team/', views.DigitalPressTeamView.as_view(), name='digital-press-team'),
    path('conference-services/', views.ConferenceServicesView.as_view(), name='conference-services'),
]
