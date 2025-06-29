from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинки')
    social_website = models.URLField(max_length=200, blank=True, null=True, verbose_name='Ссылка')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    news_view = models.IntegerField(default=0)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title} - {self.create_date}'
    
class NewsImage(models.Model):
    news =  models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.news.title

class Ads(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Обявление'
        verbose_name_plural = 'Обявление'

    def __str__(self):
        return f'{self.title}'


class About(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    info = models.TextField()

    class Meta:
        verbose_name = 'О библиотеки'
        verbose_name_plural = 'О библиотеки'

    def __str__(self):
        return self.title

class History(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

    def __str__(self):
        return str(self.id)


class Structure(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    info = models.TextField()
    img = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png',
                                verbose_name='Картинки')

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Категория'
        ordering = ('-id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(max_length=100, verbose_name='слаг')
    author = models.CharField(max_length=100, verbose_name='автор')
    year = models.CharField(max_length=100, verbose_name='год')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    pdf = models.FileField(upload_to='book/pdfs/')
    photo = models.ImageField(upload_to='book/photos/', null=True, blank=True)
    recommended_books = models.BooleanField(default=False, verbose_name='рекомендовано')
    top_books = models.BooleanField(default=False, verbose_name='топ')
    business_books = models.BooleanField(default=False, verbose_name='бизнес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('books', args=[self.slug])


class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    photo_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Photo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')



class Readers(models.Model):
    text = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатель' 


class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

class Catalog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return str(self.title)    
    

# книжный фонд
class BookFond(models.Model):
    abon_number = models.IntegerField(null=True, blank=True, verbose_name='Абономент №')
    abon_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Факультет')
    all_number = models.IntegerField(null=True, blank=True, verbose_name='Жалпы фонд саны')
    kyrgyz_num = models.IntegerField(null=True, blank=True, verbose_name='Кыргыз тилиндеги китептердин саны')
    russ_num = models.IntegerField(null=True, blank=True, verbose_name='Орус тилиндеги китептердин саны')
    inter_num = models.IntegerField(null=True, blank=True, verbose_name='Дуйнолук китептердин саны')
    eng_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Англис тилиндеги китептер')
    eng_num = models.IntegerField(null=True, blank=True, verbose_name='Англис тилиндеги китептердин саны')
    ger_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Немец тилиндеги китептер')
    ger_num = models.IntegerField(null=True, blank=True, verbose_name='Немец тилиндеги китептердин саны')
    fra_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Француз тилиндеги китептер')
    fra_num = models.IntegerField(null=True, blank=True, verbose_name='Француз тилиндеги китептердин саны')
    tur_name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Түрк тилиндеги китептер')
    tur_num = models.IntegerField(null=True, blank=True, verbose_name='Түрк тилиндеги китептердин саны')
    first_block = models.IntegerField(null=True, blank=True, verbose_name='1-блок')
    second_block = models.IntegerField(null=True, blank=True, verbose_name='2-блок')
    third_block = models.IntegerField(null=True, blank=True, verbose_name='3-блок')
    teachers_work = models.IntegerField(null=True, blank=True, verbose_name='окутуучулардын эмгектери')

    def __str__(self):
        return self.abon_name

    class Meta:
        verbose_name = 'Книжный фонд'
        verbose_name_plural = 'Книжный фонд'
        ordering = ('id',)

class SistemCatalog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    pdf = models.FileField(upload_to='catalog/pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Систематический каталог"
        verbose_name_plural = "Систематический каталог"

class Director(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField()
    img = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png',
                              verbose_name='Картинки')
    
    def __str__(self):
        return self.name
    
    