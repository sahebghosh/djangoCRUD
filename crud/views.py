from django.shortcuts import render, redirect
from .models import BookLibrary


def index(request):
    book = BookLibrary.objects.all()
    context = {
        'books': book
    }
    return render(request, 'crud/index.html', context)

def add(request):
    return render(request, 'crud/add.html')

def create(request):
    title = request.GET['name']
    author = request.GET['author']
    price = request.GET['price']
    detail = BookLibrary(name=title, author=author, price=price)
    detail.save()
    return redirect('/')

def delete(request, id):
    book = BookLibrary.objects.get(pk=id)
    book.delete()
    return redirect('/')
    
def edit(request, id):
    book = BookLibrary.objects.get(pk=id)
    context = {
        'book': book
    }
    return render(request, 'crud/edit.html', context)

def update(request, id):
    book = BookLibrary.objects.get(pk=id)
    book.title = request.GET['name']
    book.price = request.GET['price']
    book.author = request.GET['author']
    book.save()
    return redirect('/')

    