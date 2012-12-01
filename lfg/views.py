from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomepageView(TemplateView):
    template_name = "homepage.html"


def oldschool_view(request):
    template = "test.html"

    context_update = {'test':'test'}
    return render(te)