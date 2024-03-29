from .views import *
from django.urls import path

urlpatterns = [
    path('', BookListView.as_view()),
    path('book-list/', BookListView.as_view(), name='book-list'),
    path('book-create/', BookCreateView.as_view(), name='book-create'),
    path('book-detail/<int:pk>', BookDetailView.as_view(),name='book-detail'),
    path('book-update/<int:pk>', BookUpdateView.as_view(),name='book-update'),
    path('book-delete/<int:pk>', BookDeleteView.as_view(),name='book-delete'),
]