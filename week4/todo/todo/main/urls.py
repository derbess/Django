from django.urls import path

from .views import TodoListListAPIView


urlpatterns = [
    # path('works/', ),
    path('todolists/', TodoListListAPIView.as_view()),
    # path('places/', ),
]