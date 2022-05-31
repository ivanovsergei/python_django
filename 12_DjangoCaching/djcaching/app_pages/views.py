from django.shortcuts import render
from django.views import View
from time import sleep
from django.views.decorators.cache import cache_page


class MainView(View):

    def get(self, request):
        sleep(1)
        return render(request, 'main.html')


@cache_page(30)
def welcome(request, *args, **kwargs):
    sleep(2)
    return render(request, 'main.html')


def view4_decorate_in_url(request, *args, **kwargs):
    sleep(2)
    return render(request, 'main.html')
