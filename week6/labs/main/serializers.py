from rest_framework import serializers
from main.models import List, ToDo
from auth_.serializers import MyUserSerializer


class ListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = MyUserSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = List
        fields = ('id', 'name', 'created_by', 'created_at')


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    list = ListSerializer(required=False)
    status = serializers.IntegerField(required=True)

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'list', 'status')