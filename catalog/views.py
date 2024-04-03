from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render
from .models import *
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def index(request):
    """View function for home page of site."""
    # generate counts of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits
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


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )


class LoanedBooksByAllUsersListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to all users."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(status__exact='o')
            .filter(status__exact='o')
            .order_by('due_back')
        )
