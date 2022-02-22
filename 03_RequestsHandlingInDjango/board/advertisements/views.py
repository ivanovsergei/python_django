from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


def advertisement_list(request, *args, **kwargs):
    advertisements_1 = [
        '1-ый список = Мастер на час',
        '1-ый список =Выведение из запоя',
        '1-ый список =Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_2 = [
        '2-ой список =Мастер на час',
        '2-ой список =Выведение из запоя',
        '2-ой список =Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_3 = [
        '3-ий список =Мастер на час',
        '3-ий список =Выведение из запоя',
        '3-ий список =Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements_1': advertisements_1,
                                                                      'advertisements_2': advertisements_2,
                                                                      'advertisements_3': advertisements_3})


class Main(View):
    def get(self, request):
        category_lst = [
            'Ноутбуки',
            'Планшеты',
            'Телефоны',
            'Компьютеры'
        ]
        regions_lst3 = [
            'Москва',
            'Московская область',
            'республика Алтай',
            'Вологодская область'
        ]
        return render(request, 'advertisements/cbv_main.html', {'category_lst': category_lst,
                                                                'regions_lst3': regions_lst3})

    def post(self, request):
        regions_lst3 = [
            'Регион успешно создан'
        ]
        return render(request, 'advertisements/regions2.html', {'regions_lst3': regions_lst3})


def contacts(request, *args, **kwargs):
    phone_nums = [
        '8-800-708-19-45'
    ]
    emails = [
        'sales@company.com'
    ]
    return render(request, 'advertisements/contacts.html', {'phone_nums': phone_nums,
                                                            'emails': emails})


def about(request, *args, **kwargs):
    ads = [
        'Бесплатные объявления в вашем городе!',
    ]
    return render(request, 'advertisements/about.html', {'ads': ads})


def categories(request, *args, **kwargs):
    categories_lst = [
        'личные вещи',
        'транспорт',
        'хобби и отдых'
    ]
    return render(request, 'advertisements/categories.html', {'categories_lst': categories_lst})


def regions1(request, *args, **kwargs):
    regions_lst1 = [
        'Москва',
        'Московская область',
        'республика Алтай',
        'Вологодская область'
    ]
    return render(request, 'advertisements/regions1.html', {'regions_lst1': regions_lst1})


class Regions2(View):
    def get(self, request):
        regions_lst2 = [
            'Москва',
            'Московская область',
            'республика Алтай',
            'Вологодская область'
        ]
        return render(request, 'advertisements/regions2.html', {'regions_lst2': regions_lst2})

    def post(self, request):
        regions_lst2 = [
            'Регион успешно создан'
        ]
        return render(request, 'advertisements/regions2.html', {'regions_lst2': regions_lst2})


class Advertisements(View):
    COUNT = 0

    def get(self, request):
        Advertisements.COUNT += 1
        advertisements = [
            'Покупка компьютеров',
            'Покупка ноутбуков',
            'Продажа планшетов',
            'Продажа телефонов'
        ]
        return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements,
                                                                      'COUNT': Advertisements.COUNT})

    def post(self, request):
        return HttpResponse('запрос на создание новой записи успешно выполнен')


class Contacts(TemplateView):
    template_name = 'advertisements/tv_contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'г. Москва, ул. Пичугина, д. 10, офис 5А'
        context['phone_num'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'

        return context


class About(TemplateView):
    template_name = 'advertisements/tv_about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ОАО ГрантДизайн'
        context['description'] = """
        Компания основана в 1993 году... .
        """

        return context
