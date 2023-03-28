from django.shortcuts import render,HttpResponse,redirect


from .models import Book
from .forms import BookCreate
# Create your views here.


def index(request):
    shelf=Book.objects.all()
    return render(request, "index.html", {'shelf':shelf})

def upload(request):
    upload=BookCreate()
    if request.method=='POST':
        upload=BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse(""" Something went wrong, Wait for a minute""")
    else:
        return render (request, "pages/upload_form.html",{'upload_form':upload})

def update_book(request, book_id):
    book_id=int(book_id)
    try:
        book_shelf =Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_form=BookCreate(request.POST or None, instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect("home")
    return render(request, 'pages/upload_form.html', {'upload_form':book_form})

def delete_book(request,book_id):
    book_id=int(book_id)
    try:
        book_shelf =Book.objects.get(id=book_id)
        book_shelf.delete();
        shelf=Book.objects.all();
    except Book.DoesNotExist:
        return redirect('home')
    return render(request, "index.html", {'shelf':shelf})