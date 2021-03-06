from django.shortcuts import render
from p_library.models import Book
from p_library.models import Publisher
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from p_library.models import Author, Inspiration, Friend
from p_library.forms import AuthorForm
from p_library.forms import BookForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth  
from django.http.response import HttpResponseRedirect

def books_list(request):
    template = loader.get_template('books.html')
    books = Book.objects.all()
    biblio_data = {
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def publisher_list(request):
    publishers = Publisher.objects.all()
    return HttpResponse(publishers)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    inspirers = Inspiration.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "inspirers": inspirers,
    }
    if request.user.is_authenticated:  
        biblio_data['username'] = request.user.username 
    return HttpResponse(template.render(biblio_data, request))

def publishers(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    pub_data = {
        "title": "издательств",
        "publishers": publishers,
    }
    return HttpResponse(template.render(pub_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books/')
            book.copy_count += 1
            book.save()
        return redirect('/books/')
    else:
        return redirect('/books/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/books/')
    else:
        return redirect('/books/')

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'author_edit.html'  
  
class AuthorList(ListView):  
    model = Author  
    template_name = 'authors_list.html'

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:  
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  
    BookFormSet = formset_factory(BookForm, extra=2)  
    if request.method == 'POST':  
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
        if author_formset.is_valid() and book_formset.is_valid():  
            for author_form in author_formset:  
                author_form.save()  
            for book_form in book_formset:  
                book_form.save()  
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  
    else:  
        author_formset = AuthorFormSet(prefix='authors')  
        book_formset = BookFormSet(prefix='books')  
    return render(
	    request,  
		'manage_books_authors.html',  
		{  
	        'author_formset': author_formset,  
			'book_formset': book_formset,  
		}  
	)

def login(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(request=request, data=request.POST)  
        if form.is_valid():  
            auth.login(request, form.get_user())  
            return HttpResponseRedirect(reverse_lazy('p_library:index'))  
    else:  
        context = {'form': AuthenticationForm()}  
        return render(request, 'login.html', context)  
  
  
def logout(request):  
    auth.logout(request)  
    return HttpResponseRedirect(reverse_lazy('p_library:index'))