from django.http import JsonResponse
from .entities import Item
from .serializers import ItemSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Good
from .serializers import GoodSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView


def items_list(request):
    if request.method == 'GET':
        items_for_sale = [
            Item(
                name='Кофеварка',
                description='Варит отличное кофе',
                weight=100
            ),
            Item(
                name='Беспроводные наушники',
                description='Отличный звук',
                weight=150
            )
        ]
        # return JsonResponse([item.to_dict() for item in items_for_sale], safe=False)
        return JsonResponse(ItemSerializer(items_for_sale, many=True).data, safe=False)


class GoodList(APIView):
    def get(self,request):
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GoodListMixin(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)