from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    book = Books.objects
    return render(request, 'books/home.html', {'books': book})
@login_required
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['author'] and  request.POST['description'] and  request.FILES['pdf']:
            book = Books()
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.description = request.POST['description']
            book.upload_date = timezone.datetime.now()
            book.uploader = request.user

            if request.FILES['pdf'].name.endswith('.pdf'):
                book.pdf = request.FILES['pdf']
            else:
                return render(request, 'books/addbook.html', {'error': 'Upload a Valid PDF file'})
            if request.FILES['image'].name.endswith('.jpg') or request.FILES['image'].name.endswith('.png'):
                book.image = request.FILES['image']
                book.save()
                return render(request, 'books/addbook.html', {'error': 'Saved'})
            else:
                return render(request, 'books/addbook.html', {'error': 'Upload an Image with .png or .jpg'})
        else:
            return render(request, 'books/addbook.html', {'error': 'All fields are Required!'})
    else:
        return render(request, 'books/addbook.html')


def detail(request, books_id):
    book = get_object_or_404(Books, pk=books_id)
    return render(request, 'books/detail.html', {'book':book})

@login_required
def download(request, books_id):
    if request.method == 'POST':
        book = get_object_or_404(Books, pk=books_id)
        book.downloads += 1
        book.save()
        return redirect(book.pdf.url)