from django.views import generic

from .models import Committee, Staff


class IndexView(generic.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class ScheduleView(generic.TemplateView):
    template_name = 'pages/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class AboutView(generic.TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class VolMUN101View(generic.TemplateView):
    template_name = 'pages/volmun-101.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class DelegateGuidebookView(generic.TemplateView):
    template_name = 'pages/delegate-guidebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class RegistrationView(generic.TemplateView):
    template_name = 'pages/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class ConferenceHandbookView(generic.TemplateView):
    template_name = 'pages/conference-handbook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class AdvisorGuidebookView(generic.TemplateView):
    template_name = 'pages/advisor-guidebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class FeesAndAccommodationsView(generic.TemplateView):
    template_name = 'pages/fees-and-accommodations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class FeedbackView(generic.TemplateView):
    template_name = 'pages/feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class ContactUsView(generic.TemplateView):
    template_name = 'pages/contact-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class SecretariatView(generic.ListView):
    model = Staff
    template_name = 'pages/secretariat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Staff.objects.filter(positions__branches__name='Secretariat').order_by('positions__priority')
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class DigitalPressTeamView(generic.ListView):
    model = Staff
    template_name = 'pages/digital-press-team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Staff.objects.filter(positions__branches__name='Digital Press Team').order_by('positions__priority')
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class ConferenceServicesView(generic.ListView):
    model = Staff
    template_name = 'pages/conference-services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Staff.objects.filter(positions__branches__name='Conference Services').order_by('positions__priority')
        context['ga'] = Committee.objects.filter(slug='ga')
        return context
