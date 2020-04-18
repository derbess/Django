from main import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'lists', views.ListsViewSet, basename='lists')
router.register(r'todos', views.TodoViewSet, basename='todos')


urlpatterns = [
    path('lists/<int:pk>/todos/', views.ListTodosAPIView.as_view())
]

urlpatterns += router.urls