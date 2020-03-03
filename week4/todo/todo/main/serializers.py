from rest_framework import serializers

from todo.main.models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'name', 'owner')