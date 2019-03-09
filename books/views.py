from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'books/home.html')


def bookview(request):
    book_list = Books.objects.all().order_by('-upload_date')
    paginator = Paginator(book_list, 20)  # Show 20 books per page TODO improve pagination
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'books/all.html', {'books': book})


@login_required
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['author'] and request.POST['description'] and request.FILES['pdf'] and request.FILES['image']:
            book = Books()
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.description = request.POST['description']
            book.upload_date = timezone.datetime.now()
            book.uploader = request.user
            book.pdf = request.FILES['pdf']
            book.image = request.FILES['image']
            book.size = book.pdf.size
            book.save()
            return redirect('home')
        else:
            return render(request, 'books/addbook.html', {'error': 'All fields are Required!'})
    else:
        return render(request, 'books/addbook.html')


def detail(request, books_id):
    book = get_object_or_404(Books, pk=books_id)
    return render(request, 'books/detail.html', {'book': book})


def download(request, books_id):
    if request.method == 'POST':
        book = get_object_or_404(Books, pk=books_id)
        book.downloads += 1
        book.save()
        return redirect(book.pdf.url)


def search(request):
    if request.method == 'POST':
        book = Books.objects.all().filter(title__icontains=request.POST['query'])
        return render(request, 'books/search-result.html', {'books': book})



