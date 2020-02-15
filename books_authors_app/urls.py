from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book', views.create_book, name="create_book"),
    path('books/<int:id>', views.view_book, name='view_book'),
    path('books/add_author/<int:id>', views.add_author, name='add_author'),

    path('authors', views.index_authors, name="index_authors"),
    path('create_author', views.create_author, name="create_auhtor"),
    path('authors/<int:id>', views.view_author, name="view_author"),
    path('authors/add_book/<int:id>', views.add_book, name="add_book"),
]