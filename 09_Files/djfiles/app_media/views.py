from _csv import reader
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ExUploadFileForm, UploadPriceForm, ModelUploadForm, MultiFileForm
from .models import Item, File


def ex_upload_file(request):
    if request.method == 'POST':
        upload_file_form = ExUploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            forbidden_words_list = ['Это', 'слово', 'нельзя', 'использовать']
            file = request.FILES['file']
            file_name = file.name.split('.')[0]
            if file_name in forbidden_words_list:
                return HttpResponse('Это слово нельзя использовать')
            else:
                return HttpResponse(content=f'{file.name} {file.size} байт', status=200)
    else:
        upload_file_form = ExUploadFileForm()
    context = {
        'form': upload_file_form
    }

    return render(request, 'media/upload_file.html', context)


def items_list(request):
    items = Item.objects.all()
    return render(request, 'goods/items_list.html', {'items_list': items})


def update_price(request):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split()
            csv_reader = reader(price_str, delimiter=";")
            for row in csv_reader:
                print(row)
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse(content='Цены были успешно обновлены', status=200)
    else:
        upload_file_form = UploadPriceForm()

    return render(request, 'media/upload_file.html', {'form': upload_file_form})


def model_form_upload(request):
    if request.method == 'POST':
        form = ModelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ModelUploadForm()
    return render(request, 'media/file_form_upload.html', {'form': form})


def multi_file_upload(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')
    else:
        form = MultiFileForm()
    return render(request, 'media/file_form_upload.html', {'form': form})
