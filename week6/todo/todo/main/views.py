from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from todo.main.models import TodoList
from todo.main.serializers import TodoListSerializer

class TodoListListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)