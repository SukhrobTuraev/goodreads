from django.urls import path
from .views import BooksView, BookDetailView

app_name = "books"
urlpatterns = [
    path('', BooksView.as_view(), name='books-list'),
    path('<int:id>/', BookDetailView.as_view(), name='books-detail')
]