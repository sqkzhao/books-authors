from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def create_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def view_book(request, id):
    context = {
        "all_authors": Author.objects.all(),
        "book": Book.objects.get(id=id)
    }
    return render(request, 'view_book.html', context)

def add_author(request, id):
    the_book = Book.objects.get(id=id)
    selected_author = Author.objects.get(id=request.POST['author_id'])
    the_book.authors.add(selected_author)
    return redirect(f'/books/{id}')

def index_authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)

def create_author(request):
    Author.objects.create(last_name=request.POST['last_name'], first_name=request.POST['first_name'], notes=request.POST['notes'])
    return redirect('/authors')

def view_author(request, id):
    context = {
        "all_books": Book.objects.all(),
        "author": Author.objects.get(id=id)
    }
    return render(request, 'view_author.html', context)

def add_book(request, id):
    the_author = Author.objects.get(id=id)
    selected_book = Book.objects.get(id=request.POST['book_id'])
    the_author.books.add(selected_book)
    return redirect(f'/authors/{id}')