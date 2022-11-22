from django.urls import path
from .views import LibraryHomeView, BookDetailView, BookPostNew

urlpatterns = [
    path('', LibraryHomeView.as_view(), name='library-home'),
    path('detail/', BookDetailView.as_view(), name='book-detail'),
    path('new-book/', BookPostNew.as_view(), name='book-new'),
]
