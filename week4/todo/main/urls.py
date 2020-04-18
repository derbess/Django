from django.urls import path
from main import views

urlpatterns = [
    path('lists/', views.ListsAPIView.as_view()),
    path('lists/<int:pk>/', views.ListAPIView.as_view()),
    path('lists/<int:pk>/todos/', views.TodosAPIView.as_view()),
    path('todos/<int:pk>/', views.TodoAPIView.as_view())
]