from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

# Create your views here.


def book_list(request):
    books=Book.objects.all()
    return render(request,'books/book_list.html',{'books':books})

def add_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        
    else:
        form=BookForm()
    
    return render(request,'books/add_book.html',{'form':form})

def edit_book(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm(instance=book)
    
    return render(request,'books/edit_book.html',{'form':form})

def delete_book(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method=="POST":
        book.delete()
        return redirect('book_list')
    
    return render(request,'books/delete_book.html',{'book':book})