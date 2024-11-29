from django.shortcuts import render, redirect,get_object_or_404
from django.template.context_processors import request

from .forms import Authorform,Bookform
# Create your views here.


from.models import Book

# function based view
# def create_book(request):
#     books = Book.objects.all()
#
#     if request.method =='POST':
#         title=request.POST.get('title')
#         price = request.POST.get('price')
#
#         book=Book(title=title,price=price)
#
#         book.save()
#
#     return render(request,'book.html',{'books':books})

def listBook(request):
    books =Book.objects.all()
    return  render(request,'listbook.html',{'books':books})



def detailsView(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'detailsview.html',{'book':book})


# def updateBook(request,book_id):
#     book=Book.objects.get(id=book_id)
#
#     if request.method =='POST':
#         title=request.POST.get('title')
#         price = request.POST.get('price')
#
#         book.title=title
#         book.price=price
#         book.save()
#         return redirect('/')
#     return render(request,'updateview.html',{'book':book})


def delview(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method =="POST":
        book.delete()
        return redirect('/')

    return  render(request,'delview.html',{'book':book})

def create_book(request):
    books =Book.objects.all()
    if request.method =="POST":
        form = Bookform(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form =Bookform()

    return render(request,'book.html',{'form':form,'books':books})

def create_author(request):
    if request.method =="POST":
        form = Authorform(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form =Authorform()

    return render(request,'author.html',{'form':form})

def updateBook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method == "POST":
        form = Bookform(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form =Bookform(instance=book)

    return render(request,'updateview.html',{'form':form})


# def updateBook(request, book_id):
#     # Correct the lookup for the primary key
#     book = get_object_or_404(Book, id=book_id)
#
#     if request.method == "POST":
#         form = Bookform(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = Bookform(instance=book)
#
#     return render(request, 'updateview.html', {'form': form})


def index(request):
    return render(request,'base.html')

