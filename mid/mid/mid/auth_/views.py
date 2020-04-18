import json
from rest_framework import generics
from rest_framework.permissions import AllowAny
from mid.auth_.serializers import MyUserSerializer

from mid.auth_.models import MyUser


class MyUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all()


#
# @csrf_exempt
# def login(request):
#     body = json.loads(request.body.decode('utf-8'))
#     username = body.get('username')
#     password = body.get('password')
#
#     user = auth.authenticate(username=username, password=password)
#
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return JsonResponse({'message': 'logged in'}, status=200)
#
#     else:
#         return JsonResponse({'message': 'user not found or not active'}, status=200)
#
#
# @csrf_exempt
# def logout(request):
#     user = auth.logout(request)
#
#     return JsonResponse({'message': 'logged out'}, status=200)
#
#
# @csrf_exempt
# def register(request):
#     body = json.loads(request.body.decode('utf-8'))
#     username = body.get('username')
#     password = body.get('password')
#
#     user = MyUser.objects.create_user(username=username)
#     user.set_password(password)
#     user.save()
#
#     return JsonResponse({'message': 'registred'}, status=200)