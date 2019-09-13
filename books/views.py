from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, Type
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Tag
User = get_user_model()


# Create your views here.
def home(request):
    # This function is called when the homepage is visited. Returns the content of home.html file
    return render(request, 'books/home.html')


def view_all(request):
    # Displays all available documents, regardless of their type, ordered in reverse by upload date
    book_list = Document.objects.all().order_by('-upload_date')
    # Takes all 'document' objects in and groups them in 20's per page
    # TODO improve pagination
    paginator = Paginator(book_list, 20)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'books/all.html', {'books': book})


def books_view(request):
    # Same function as the view_all function, but restricted to Document
    book_list = Document.objects.filter(typology__name__icontains='Book').order_by('-upload_date')
    paginator = Paginator(book_list, 20)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'books/books.html', {'books': book})


def notes_view(request):
    # Same function as the view_all function, but restricted to Notes
    book_list = Document.objects.filter(typology__name__icontains='Note').order_by('-upload_date')
    paginator = Paginator(book_list, 20)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'books/notes.html', {'books': book})


def question_view(request):
    # Same function as the view_all function, but restricted to Questions
    book_list = Document.objects.filter(typology__name__icontains='Question').order_by('-upload_date')
    paginator = Paginator(book_list, 20)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'books/questions.html', {'books': book})


@login_required
def add(request):
    # This function is called by the add a document page, POST method runs a few checks and saves the document is
    # successful. Checks if any book exists with the same title and author, if yes, return a 'document already
    # exists message
    if request.method == 'POST':
        if Document.objects.filter(title__iexact=request.POST['title']) and \
                Document.objects.filter(author__iexact=request.POST['author']):
            message = {
                'error_exists': 'Document already Exists',
                'classification': Type.objects.all()
            }
            return render(request, 'books/add-a-document.html', {'dict': message})
        else:
            book = Document()
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.description = request.POST['description']
            book.upload_date = timezone.datetime.now()
            book.uploader = request.user
            # Validates files to be uploaded
            if request.FILES.get('image', False):
                if request.FILES['image'].name.endswith('.jpg') or request.FILES['image'].name.endswith('.png'):
                    book.image = request.FILES['image']
                else:
                    message = {
                        'error_image': 'Upload a Valid Image. PNG or JPG',
                        'classification': Type.objects.all()
                    }
                    return render(request, 'books/add-a-document.html', {'dict': message})
            
            name = request.FILES['pdf'].name
            formats = ['pdf', 'epub', 'docx', 'doc', 'ppt']
            if name.rsplit('.')[-1] in formats:
                book.pdf = request.FILES['pdf']
            else:
                message = {
                    'error_file': 'Supported formats are PDF, EPUB, PPT, DOC, DOCX',
                    'classification': Type.objects.all()
                }
                return render(request, 'books/add-a-document.html', {'dict': message})
            # End of validation
            book.size = book.pdf.size
            user = User.objects.get(pk=book.uploader_id)
            user.profile.points += 6
            user.profile.save()
            category = request.POST.get('category')
            typology = Type.objects.get(name__icontains=category)
            book.typology = typology
            book.save()
            tag_profile(request, book)
            return render(request, 'books/add-a-document.html', {'word': 'Upload Successful. Upload another 😉'})
    
    else:
        message = {
            'classification': Type.objects.all()
        }
        return render(request, 'books/add-a-document.html', {'dict': message})


def tag_profile(request, book):
    all_tags = request.POST['tag'].split(',')
    new_list = []
    for i in all_tags:
        new_list.append(i.strip())

    for x in new_list:
        if Tag.objects.filter(name__iexact=x).exists():
            tag = Tag.objects.get(name__iexact=x)
            book.tags.add(tag)
        else:
            Tag.objects.create(name=x)
            tag = Tag.objects.get(name__iexact=x)
            book.tags.add(tag)


def detail(request, slug):
    if request.method == 'POST':
        book = get_object_or_404(Document, slug=slug)
        tag_profile(request, book)
        return redirect('detail', slug)
    else:
        book = get_object_or_404(Document, slug=slug)
        return render(request, 'books/detail.html', {'book': book})


def download(request, slug):
    if request.method == 'POST':
        book = get_object_or_404(Document, slug=slug)
        user = User.objects.get(pk=book.uploader_id)
        user.profile.points += 2
        user.profile.save()
        book.downloads += 1
        book.save()
        return redirect(book.pdf.url)


def search(request):
    if request.method == 'POST':
        query = request.POST['query']
    else:
        query = request.GET['query']
    books = Document.objects.all().filter(title__icontains=query).order_by('-downloads')
    authors = Document.objects.all().filter(author__icontains=query).order_by('-downloads')
    tags = Document.objects.all().filter(tags__name__icontains=query).order_by('-downloads')
    book_list = (books | authors | tags).distinct()
    paginator = Paginator(book_list, 20)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'books/search-result.html', {'books': book, 'query': query})


def sitemap(request):
    tag_list = Tag.objects.all().order_by('name')
    return render(request, 'books/all-tags.html', {'tags': tag_list})
