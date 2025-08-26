from django.shortcuts import render, HttpResponse
from .forms import BookForm
from .models import Books
from django.db.models import Avg, Min, Max, Sum, Count

def index(request):
    bookform=BookForm()
    if request.method=='POST':
        bookform=BookForm(request.POST)
        if bookform.is_valid():
            bookform.save()
            title=bookform.cleaned_data['title']
            author=bookform.cleaned_data['author']
            published_year=bookform.cleaned_data['published_year']
            cost=bookform.cleaned_data['cost']
            pages=bookform.cleaned_data['pages']
            genre=bookform.cleaned_data['genre']
            return HttpResponse(f'Информация о книге: название-{title}, автор-{author}, год публикации-{published_year}, стоимость-{cost}, кол-во страниц-{pages}, жанр-{genre}')
    return render(request,'index.html', {'form':bookform})

def filter(request):
    books=Books.objects.all()
    books_count=books.count()

    avg_cost=books.aggregate(Avg('cost'))

    max_cost=books.aggregate(Max('cost'))
    min_cost=books.aggregate(Min('cost'))

    sum_pages=books.aggregate(Sum('pages'))

    books_count_genre=books.annotate(count_genre=Count('genre'))
    books_count_fantasy=books_count_genre[0].count_genre
    books_count_sci_fi=books_count_genre[1].count_genre
    books_count_mystery=books_count_genre[2].count_genre
    books_count_horror=books_count_genre[3].count_genre
    books_count_non_fiction=books_count_genre[4].count_genre

    form={'books_count':books_count,
          'avg_cost':avg_cost,
          'max_cost':max_cost,
          'min_cost':min_cost,
          'sum_pages':sum_pages,
          'books_count_fantasy':books_count_fantasy,
          'books_count_sci_fi':books_count_sci_fi,
          'books_count_mystery':books_count_mystery,
          'books_count_horror':books_count_horror,
          'books_count_non_fiction':books_count_non_fiction,
          
    }
    return render(request, 'filter.html', {'form':form})

