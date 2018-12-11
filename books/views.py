from django.shortcuts import render, redirect
from .models import books

# Create your views here.
def home(request):
    booklist = books.objects
    return render(request, 'books/home.html', {'books': booklist})

def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['author'] and  request.POST['description'] and  request.FILES['pdf']:
            book = books()
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.description = request.POST['description']

            if request.FILES['pdf'].name.endswith('.pdf'):
                book.pdf = request.FILES['pdf']
            else:
                return render(request, 'books/addbook.html', {'error': 'Upload a Valid PDF file'})
            if request.FILES['image'].name.endswith('.jpg') or request.FILES['image'].name.endswith('.png'):
                book.image = request.FILES['image']
            else:
                return render(request, 'books/addbook.html', {'error': 'Upload an Image with .png or .jpg'})
            book.save()
            return redirect(request, 'books/addbook.html')
        else:
            return render(request, 'books/addbook.html', {'error': 'All fields are Required!'})
    else:
        return render(request, 'books/addbook.html')
