import random
from django.shortcuts import render
from django.views import generic
from ads.models import Advertisement


def advertisement(request, *args, **kwargs):
    count_ads = Advertisement.objects.count()
    random_ad = random.randint(1, count_ads)
    adv = Advertisement.objects.get(pk=random_ad)
    return render(request, 'advertisements/advertisement.html', {
        'advertisement': adv,
    })


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements/advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:10]


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'
