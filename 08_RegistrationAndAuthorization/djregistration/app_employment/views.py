from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import Vacancy


def vacancy_list(request):
    if not request.user.has_perm('app_employment.view_vacancy'):
        raise PermissionDenied()
    vacancies = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})
