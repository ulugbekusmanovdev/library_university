from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import NewsForm
from .utils import check_read_articles

#multilanguage
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

# multilanguage code end

# Create your views here.
def homepage(request):
    books = Book.objects.all().order_by('-id')[0:5]
    news = News.objects.all().order_by('-create_date')[0:3]
    last_news = News.objects.order_by('-create_date').first()
    adt = Ads.objects.all().order_by('-id')[0:3]
    structure = Structure.objects.all()
    about = About.objects.all()
    history = History.objects.filter(id=3)
    history1 = History.objects.filter(id=4)
    videos = Video.objects.all()
    context = {'news': news, 'last_news': last_news, 'adt': adt, 'structure': structure,
                'about': about, 'books': books, 'videos': videos,
                'history': history, 'history1': history1}
    return render(request, 'home.html', context)


def news(request):
    news = News.objects.all()

    contex = {'news': news}
    return render(request, 'news.html', contex)


def adt(request):
    adt = Ads.objects.all()
    contex = {'adt': adt}
    return render(request, 'adt.html', contex)


def readers(request):
    
    readers = Readers.objects.all()
    context = { 'readers': readers}
    return render(request, 'readers.html', context) 


def catalog(request):
    bookfond = BookFond.objects.all()

    # topSkills = profile.skill_set.exclude(description__exact='')
    
    context = {'bookfond': bookfond}
    return render(request, 'catalog.html', context)


def structure(request):
    pass


def categories(request):
    categories = Category.objects.all().order_by('id')[0:12]
    categories1 = Category.objects.all().order_by('id')[12:23]
    categories2 = Category.objects.all().order_by('id')[23:43]

    return {'categories': categories, 'categories1': categories1, 'categories2': categories2}


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    books = Book.objects.filter(category=category)
    return render(request, 'list-category.html', {'category': category, 'books': books})


def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)


def search(request):
    search = request.GET.get('q', '').lower()

    if search:
        books = Book.objects.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(category__name__icontains=search)
        )
    else:
        books = Book.objects.all().order_by('-id')
    return render(request, 'books.html', {"books": books})


def photo(request):
    photos = Photo.objects.all()
    return render(request, 'photo.html', {'photos': photos})


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    return render(request, 'single_photo.html', {'photo': photo})



def video(request):
    return render(request, 'video.html')

def magazine(request):
    return render(request, 'magazine.html')

def gazeta(request):
    return render(request, 'gazeta.html')

def profs(request):
    return render(request, 'profsoyz.html')

def kfond(request):
    catalog_list = SistemCatalog.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        pdf = request.FILES.get('pdf')

        if title and pdf:
            SistemCatalog.objects.create(title=title,pdf=pdf)
            return redirect('kfond')


    b_catalog = Catalog.objects.filter(id=1)
    el_catalog = Catalog.objects.filter(id=2)
    context = {'b_catalog': b_catalog, 'el_catalog': el_catalog, 'catalog_list': catalog_list}
    return render(request, 'kfond.html', context)

def bibliograf(request):
    return render(request, 'bibliograf.html')

def calendar(request):
    return render(request, 'calendar.html')

def bibizdanie(request):
    return render(request, 'bibizdanie.html')

def question(request):
    return render(request, 'question.html')

def technique(request):
    return render(request, 'technique.html')

def news1(request, pk):
    single_news = News.objects.get(id=pk)

    request.session.modified = True
    if single_news.id in check_read_articles(request):
        pass
    else:
        check_read_articles(request).append(single_news.id)
        single_news.news_view += 1
        single_news.save()

    context = {'single_news': single_news}
    return render(request, 'news1.html', context)

def strukture(request):
    director = Director.objects.all()
    structure = Structure.objects.all()
    structure1 = Structure.objects.filter(id=1)
    structure2 = Structure.objects.filter(id=2)
    structure3 = Structure.objects.filter(id=3)

    context = {'structure1': structure1, 'structure2': structure2, 
               'structure3': structure3, 'director': director}
    return render(request, 'strukture.html', context)

# def createNews(request):
#     newsform = NewsForm()
#     imageform = ImageForm()

#     if request.method == 'POST':
#         files = request.FILES.getlist('images')
#         newsform = NewsForm(request.POST, request.FILES)
#         if newsform.is_valid():
#             news = newsform.save(commit=False)
#             news.save()

#             for file in files:
#                 NewsImage.objects.create(news=news, images=files)
            
#             return redirect('news/')

#     context = {'n_form': newsform, 'i_form': imageform}
#     return render(request, 'createnews.html', context)


