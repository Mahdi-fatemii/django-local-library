from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', login_required(views.LoanedBooksByUserListView.as_view()), name='my-borrowed'),
    path('allbooks/', views.LoanedBooksByAllUsersListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', staff_member_required(views.AuthorCreate.as_view()), name='author-create'),
    path('book/create/', staff_member_required(views.BookCreate.as_view()), name='book-create'),
    path('author/<int:pk>/update/', staff_member_required(views.AuthorUpdate.as_view()), name='author-update'),
    path('book/<int:pk>/update/', staff_member_required(views.BookUpdate.as_view()), name='book-update'),
    path('author/<int:pk>/delete/', staff_member_required(views.AuthorDelete.as_view()), name='author-delete'),
    path('book/<int:pk>/delete/', staff_member_required(views.BookDelete.as_view()), name='book-delete'),
]
