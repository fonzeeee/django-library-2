from django.shortcuts import render
from django.views.generic import TemplateView

class LibraryHomeView(TemplateView):
    template_name = 'books/home.html'
    

class BookDetailView(TemplateView):
    template_name = 'books/book_detail.html'
    

class BookPostNew(TemplateView):
    template_name = 'books/book_postnew.html'