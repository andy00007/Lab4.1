from django.http import HttpResponse
from django.shortcuts import render_to_response
from addr_book.models import *
import datetime
def test(request):
    authors = Author.objects.all()
    return render_to_response('test.html',{'authors':authors})

def index(request):
    book_list = Book.objects.all()
    return render_to_response('index.html',{'book_list':book_list}) 

def library(request):
    book_list = Book.objects.all()
    return render_to_response('library.html',{'book_list':book_list})    

def book(request,offset):
    book = Book.objects.get(isbn=offset)
    return render_to_response('book.html',{'book':book})

def search(request):
    if 'q' in request.GET:
       q = request.GET['q']
       if q:
          author = Author.objects.get(name=q)
          book_list = Book.objects.filter(authorid = author)
          return render_to_response('library.html',{'book_list':book_list})

def delete(request,offset):
    d = Book.objects.get(isbn=offset)
    d.delete()
    book_list = Book.objects.all()
    return render_to_response('index.html',{'book_list':book_list})

def change(request,offset):
    book = Book.objects.get(isbn=offset)
    author_list = Author.objects.all()
    return render_to_response('changeInfo.html',{'book':book,'author_list':author_list})

def update(request,offset):
    if 'a' in request.GET:
       a = request.GET['a']
       if a:
          author = Author.objects.get(name=a)
          Book.objects.filter(isbn=offset).update(authorid=author)
    if 'p' in request.GET:
       p = request.GET['p']
       if p :
          Book.objects.filter(isbn=offset).update(publisher=p)
    if 'd' in request.GET:
       d = request.GET['d']
       if d :
          Book.objects.filter(isbn=offset).update(publishdate=d)
    if 'v' in request.GET:
       v = request.GET['v']
       if v :
          Book.objects.filter(isbn=offset).update(price=v)
    book_list = Book.objects.all()
    return render_to_response('index.html',{'book_list':book_list})

def addBook(request):
    author_list=Author.objects.all()
    return render_to_response('addBook.html',{'author_list':author_list})

def addAuthor(request): 
    return render_to_response('addAuthor.html')

def addTodb(request):
     if 'i' in request.GET:
       i = request.GET['i']
     if 'n' in request.GET:
       n = request.GET['n']
     if 'a' in request.GET:
       a = request.GET['a']
     if 'c' in request.GET:
       c = request.GET['c']
     author = Author(authorid=i,name=n,age=a,country=c)
     author.save()
     return render_to_response('close.html')

def addBookView(request):
     if 't' in request.GET:
       t = request.GET['t']
     if 'i' in request.GET:
       i = request.GET['i']
     if 'a' in request.GET:
       a = request.GET['a']
       author = Author.objects.get(name=a)
     if 'p' in request.GET:
       p = request.GET['p']
     if 'd' in request.GET:
       d = request.GET['d']
     if 'v' in request.GET:
       v = request.GET['v']
     book = Book(isbn=i,authorid=author,title=t,publisher=p,publishdate=d,price=v)
     book.save()
     
     book_list = Book.objects.all()
     return render_to_response('index.html',{'book_list':book_list}) 

def authors(request):
    author_list = Author.objects.all()
    return render_to_response('authors.html',{'author_list':author_list})
