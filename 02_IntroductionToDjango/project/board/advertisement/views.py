from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement.html', {})


def programming(request, *args, **kwargs):
    return render(request, 'advertisement/programming.html', {})


def design(request, *args, **kwargs):
    return render(request, 'advertisement/design.html', {})


def marketing(request, *args, **kwargs):
    return render(request, 'advertisement/marketing.html', {})


def management(request, *args, **kwargs):
    return render(request, 'advertisement/management.html', {})


def games(request, *args, **kwargs):
    return render(request, 'advertisement/games.html', {})
