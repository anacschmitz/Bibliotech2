from django.urls import path
from BiblioTech import views

urlpatterns = [
  path('home/', views.index, name='home'),
  path('', views.index, name='home'),
  path('search-book/', views.search_book, name='search-book'),
  path('book_detail/<int:id>', views.book_detail, name='book-detail'),
  path('emprestar/<int:id>', views.emprestar, name='emprestar-livro'),
  path('devolver/<int:id>', views.devolver, name='devolver-livro'),


  # path('add-student/', views.add_estudante, name='add-student'),
  ]