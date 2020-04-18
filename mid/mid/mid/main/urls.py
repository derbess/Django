from django.urls import path

#
# urlpatterns = [
#     path('authors/', AuthorListAPIView.as_view()),
#     # path('authors/top-ten/', AuthorListAPIView.as_view()),
#     # path('authors/<int:author_id>/', AuthorDetailAPIView.as_view())
# ]
from mid.main.views_viewsets import  BookListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books', BookListViewSet)

urlpatterns = router.urls
