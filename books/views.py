from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, Faculty, Type, Level
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
        if Books.objects.filter(title__iexact=request.POST['title']) and \
                Books.objects.filter(author__iexact=request.POST['author']):
            diction = {
                'error': 'Document already Exists',
                'faculties': Faculty.objects.all(),
                'levels': Level.objects.all(),
                'classification': Type.objects.all()
            }
            return render(request, 'books/addbook.html', {'dict': diction})
        else:
            book = Books()
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.description = request.POST['description']
            book.upload_date = timezone.datetime.now()
            book.uploader = request.user
            book.pdf = request.FILES['pdf']
            book.image = request.FILES['image']
            book.size = book.pdf.size
            user = User.objects.get(pk=book.uploader_id)
            user.profile.points += 6
            user.profile.save()
            category = request.POST.get('category')
            typology = Type.objects.get(name__icontains=category)
            book.typology = typology
            book.save()
            for i in request.POST.getlist('faculty'):
                me = Faculty.objects.get(name__icontains=i)
                book.faculty.add(me)

            for i in request.POST.getlist('level'):
                lvl = Level.objects.get(name__icontains=i)
                book.level.add(lvl)
            return redirect('home')
    else:

        diction = {
            'faculties': Faculty.objects.all(),
            'levels': Level.objects.all(),
            'classification': Type.objects.all()
        }
        return render(request, 'books/addbook.html', {'dict': diction})


def detail(request, slug):
    book = get_object_or_404(Books, slug=slug)
    return render(request, 'books/detail.html', {'book': book})


def download(request, slug, books_id):
    if request.method == 'POST':
        book = get_object_or_404(Books, slug=slug, pk=books_id)
        user = User.objects.get(pk=book.uploader_id)
        user.profile.points += 2
        user.profile.save()
        book.downloads += 1
        book.save()
        return redirect(book.pdf.url)


def search(request):
    if request.method == 'POST':
        book = Books.objects.all().filter(title__icontains=request.POST['query'])
        return render(request, 'books/search-result.html', {'books': book})


def faculty(request):
    faculties = Faculty.objects.all()
    return render(request, 'books/faculties.html', {'cat': faculties})


