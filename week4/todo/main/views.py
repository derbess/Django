from main.models import List, ToDo

from main.serializers import ListSerializer, TodoSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class ListsAPIView(generics.ListCreateAPIView):
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return List.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ListAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return List.objects.for_user(user=self.request.user)

class TodosAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            list = List.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except List.DoesNotExist:
            raise Http404
        return list.todos.all()

    def perform_create(self, serializer):
        try:
            list = List.objects.get(id=self.kwargs['pk'])
        except List.DoesNotExist:
            raise Http404
        serializer.save(list = list)

class TodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDo.objects.all()