from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('news/', views.news, name='news'),
    path('adt/', views.adt, name='adt'),
    path('readers/', views.readers, name='readers'),
    path('catalog/', views.catalog, name='catalog'),
    path('structure/', views.structure, name='structure'),
    path('books/', views.books, name='books'),
    path('search', views.search, name='search'),
    path('photo/', views.photo, name='photo'),
    path('video/', views.video, name='video'),
    path('magazine/', views.magazine, name='magazine'),
    path('gazeta/', views.gazeta, name='gazeta'),
    path('profs/', views.profs, name='profs'),
    path('kfond/', views.kfond, name='kfond'),
    path('bibliograf/', views.bibliograf, name='bibliograf'),
    path('calendar/', views.calendar, name='calendar'),
    path('bibizdanie/', views.bibizdanie, name='bibizdanie'),
    path('question/', views.question, name='question'),
    path('detail/<int:pk>/', views.news1, name='detail'),
    path('strukture', views.strukture, name='strukture'),
    # path('createNews', views.createNews, name="createNews"),

    path('photo_detail/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),

    path("<str:language>", views.set_language, name="set-language"),
]