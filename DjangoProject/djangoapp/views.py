from django.shortcuts import render, HttpResponse
from .forms import BookForm, CompanyForm, ProductForm
from .models import Books, Product, Company
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

    books_count_genre=books.values('author').annotate(cost=Count('*'))
    for i in books_count_genre:
        print(f'Автор {i['author']}, Кол-во книг: {i['cost']}')
    print(books_count_genre[0]['cost'])
    # books_count_fantasy=books_count_genre[0].count_genre
    # books_count_sci_fi=books_count_genre[1].count_genre
    # books_count_mystery=books_count_genre[2].count_genre
    # books_count_horror=books_count_genre[3].count_genre
    # books_count_non_fiction=books_count_genre[3].count_genre
    # books_cost_avg=books.values('author').annotate()
    # print(books_cost_avg)
    # rouling_books_cost=books_cost_avg[0].avg_cost
    # antony_books_cost=books_cost_avg[1].avg_cost
    # haksly_books_cost=books_cost_avg[2].avg_cost


    form={'books_count':books_count,
          'avg_cost':avg_cost,
          'max_cost':max_cost,
          'min_cost':min_cost,
          'sum_pages':sum_pages,
    }
    return render(request, 'filter.html', {'form':form})

def index1(request):
    # company_create=Company.objects.create(name='Masda')
    # delete=Company.objects.filter(id=3).delete()
    # company_create.product_set.create(name='car', price=10000)
    name=Product.objects.get(id=3).company.name
    print(name)
    return HttpResponse()

def index_create(request):
    companyform=CompanyForm()
    if request.method=='POST':
        companyform=CompanyForm(request.POST)
        if companyform.is_valid():
            companyform.save()
            name=companyform.cleaned_data['name']
            return HttpResponse(f'Информация о компании: название-{name}')
    return render(request,'index_create.html', {'form':companyform})

def index_create_product(request):
    productForm=ProductForm()
    if request.method=='POST':
        productForm=ProductForm(request.POST)
        if productForm.is_valid():
            productForm.save()
            name=productForm.cleaned_data['name']
            price=productForm.cleaned_data['price']
            return HttpResponse(f'Информация о компании: название-{name}, стоимость-{price}')
    return render(request,'index_create_product.html', {'form':productForm})