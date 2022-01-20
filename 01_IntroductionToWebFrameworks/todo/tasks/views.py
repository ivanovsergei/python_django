from django.http import HttpResponse
from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        lst = ['<li>1</li>', '<li>2</li>', '<li>3</li>', '<li>4</li>', '<li>5</li>', '<li>6</li>',
               '<li>7</li>', '<li>8</li>', '<li>9</li>', '<li>10</li>']

        random_res = (random.choices(lst, k=5))
        for i in random_res:
            print(i)
        print(random_res)
        return HttpResponse(random_res)
