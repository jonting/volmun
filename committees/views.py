from django.views import generic

from .models import Committee


class IndexView(generic.ListView):
    model = Committee
    template_name = 'committees/committees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_crisis_committees'] = Committee.objects.filter(full_crisis=True)
        context['standard_committees'] = Committee.objects.exclude(full_crisis=True)
        context['ga'] = Committee.objects.filter(slug='ga')
        return context


class DetailView(generic.DetailView):
    model = Committee
    template_name = 'committees/committee_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = self.object.staff.all().filter(positions__branches__name='Committee Staff').order_by('positions__priority')
        context['ga'] = Committee.objects.filter(slug='ga')
        return context
