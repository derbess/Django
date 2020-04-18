from django.urls import path
from auth_ import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register)
]