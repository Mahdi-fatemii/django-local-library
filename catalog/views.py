from django.http import Http404
from django.shortcuts import render
from .models import *
from django.views import generic
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    """View function for home page of site."""
    # generate counts of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # your own name for the list as a template variable
    queryset = Book.objects.all()  # Get 5 books containing the title war
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'  # your own name for the list as a template variable
    queryset = Author.objects.all()  # Get 5 books containing the title war
    template_name = 'catalog/author_list.html'  # Specify your own template name/location
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})
