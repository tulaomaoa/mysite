from django.shortcuts import render,redirect, HttpResponse
from mylibrary import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

#展示出版社列表
def publisher_list(request):
    ret = models.Publisher.objects.all().order_by('id')
    return render(request,'publisher.html',{'publisher_list':ret})

#添加新的出版社
def add_publisher(request):
    error_msg = ''
    if request.method == 'POST':

        new_name = request.POST.get('publisher_name')
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')

        else:
            error_msg = "出版社名字不能为空"
    return render(request,'add_publisher.html',{'error':error_msg})


    return render(request,'add_publisher.html')

#删除出版社的函数
def delete_publisher(request):
    del_id = request.GET.get('id',None)

    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse("要删除的数据不存在")

#编辑出版社

def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.POST.get('id')
        new_name = request.POST.get('publisher_name')
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()
        return redirect('/publisher_list/')


    edit_id = request.GET.get('id')
    if edit_id:
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request,'edit_publisher.html',{'publisher':publisher_obj})
    else:
        return HttpResponse('编辑的出版社不存在')

#展示书的列表

def book_list(request):
    all_book = models.Book.objects.all()
    # return render(request,'book_list.html',{'all_book':all_book})



    paginator = Paginator(all_book, 3)
    page = request.GET.get('page','1')
    books = paginator.get_page(page)

    return render(request, 'book_list.html', {"books_list": books,
                                              "all_book":all_book})

#添加书籍
def add_book(request):
    if request.method == 'POST':
        new_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')
        #publisher_obj = models.Publisher.objects.get(id=new_publisher_id)
        #models.Book.objects.create(title=new_title,publisher=publisher_obj)

        models.Book.objects.create(title = new_title,publisher_id=new_publisher_id)
        return redirect("/book_list/")
    ret = models.Publisher.objects.all()
    return render(request,'add_book.html',{"publisher_list":ret})


#删除书籍
def delete_book(request):
    delete_id = request.GET.get('id')
    models.Book.objects.get(id=delete_id).delete()
    return redirect('/book_list/')


#编辑书籍
def edit_book(request):
    if request.method == 'POST':
        edit_id = request.POST.get('id')
        new_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id = new_publisher_id
        edit_book_obj.save()
        return redirect('/book_list/')
    edit_id = request.GET.get('id')
    edit_book_obj = models.Book.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    return render(request,
                  'edit_book.html',
                  {'publisher_list':ret,'book_obj':edit_book_obj}
                  )


#作者

def author_list(request):
    #author_obj = models.Author.objects.get(id=1)

    all_author = models.Author.objects.all()
    return render(request,'author_list.html',{'author_list':all_author})


#添加作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        new_author_obj=models.Author.objects.create(name = new_author_name)
        new_author_obj.book.set(books)

        return redirect('/author_list/')
    ret = models.Book.objects.all()
    return render(request,"add_author.html",{"book_list":ret})


#删除作者

def delete_author(request):
    delete_id = request.GET.get('id')
    models.Author.objects.get(id = delete_id).delete()
    return redirect("/author_list/")


#编辑作者

def edit_author(request):
    if request.method == 'POST':
        edit_author_id = request.POST.get('author_id')

        new_author_name = request.POST.get('author_name')
        new_books = request.POST.getlist("books")
        edit_author_obj = models.Author.objects.get(id=edit_author_id)

        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)
        edit_author_obj.save()

        return redirect('/author_list/')

    edit_id = request.GET.get('id')
    edit_author_obj = models.Author.objects.get(id= edit_id)
    ret = models.Book.objects.all()
    return render(request,'edit_author.html',{'book_list':ret, "author":edit_author_obj })


def homepage(request):
    return render(request,'homepage.html')

# def list(request):
#     books_list = models.Book.objects.all()
#     paginator = Paginator(books_list,1)
#     page = request.GET.get('page')
#     try:
#         books = paginator.page(page)
#     except PageNotAnInteger:
#         books = paginator.page(1)
#     except EmptyPage:
#         books = paginator.page(paginator.num_pages)
#     return render(request,'list.html',{"books_list":books})








