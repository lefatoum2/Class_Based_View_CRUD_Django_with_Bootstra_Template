from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ('title', 'description', 'author', 'year')
    success_url = reverse_lazy('book-list')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ('title', 'description', 'author', 'year')
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book-list')
