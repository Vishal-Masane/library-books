from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Book
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def welcome_page(request):
    return render(request, "home.html")

@login_required
def show_books(request):
    active_books = Book.objects.filter(is_active= True)
    return render(request, "show_books.html", {"all_books": active_books})

@login_required
def inactive_books(request):
    all_inactive_books = Book.objects.filter(is_active= False)
    return render(request, "inactive_books.html", {"inactive_books": all_inactive_books})

@login_required
def single_book(request, bid):
    book = Book.objects.get(id=bid)
    return render(request, "single_book.html", {"book": book})

@login_required
def add_book(request):
    print(request.POST)
    if request.method == "POST":
        book_dict = request.POST
        bname = book_dict.get("fname")
        bprice = book_dict.get("fprice")
        bqty = book_dict.get("fqty")
        bispub = book_dict.get("fispub")
        if bispub == "Yes":
            is_pub = True
        else:
            is_pub = False
        
        Book.objects.create(name=bname, price=bprice, qty=bqty, is_published=is_pub)
        messages.success(request, "Book has been added successfully..!" )
        return redirect("show_books")
    if request.method == "GET":
        return render(request, "add_book.html")
     
@login_required
def update_book(request, bid):
    u_book= Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "update_book.html", {"update_book": u_book})
    elif request.method == "POST":
        book_dict = request.POST
        bname = book_dict.get("fname")
        bprice = book_dict.get("fprice")
        bqty = book_dict.get("fqty")
        bispub = book_dict.get("fispub")
        if bispub == "Yes":
            is_pub = True
        else:
            is_pub = False
        
        u_book.name = bname
        u_book.price = bprice
        u_book.qty = bqty
        u_book.is_published = is_pub
        u_book.save()
        messages.success(request, f"Book: {u_book.name} has been updated successfully..!" )
        return redirect("show_books")
    
@login_required    
def book_hard_delete(request, bid):
    d_book= Book.objects.get(id=bid)
    d_book.delete()
    return redirect("show_books")

@login_required    
def book_soft_delete(request, bid):
    d_book= Book.objects.get(id=bid)
    d_book.is_active = False
    d_book.save()
    return redirect("show_books")

# ------------------------------------ for Form


from .forms import GeeksForm, BookForm, AddressForm
  
# Create your views here.
# def form_view(request):
#     return render(request, "form_test.html", {"form": GeeksForm()}

@login_required                  
def form_view(request):
    if request.method == "POST":
        data = request.POST
        form = BookForm(data)
        if form.is_valid:
            form.save()
        else:
            print("Enter data is not valid")
        return redirect("show_books")
    elif request.method == "GET":
        return render(request, "book_form_test.html", {"bookform": BookForm()})


"""
    <!-- <div class="form-row">
        <div class="form-group col-md-6 mb-0">
          {{ form.email|as_crispy_field }}
        </div>
        <div class="form-group col-md-6 mb-0">
          {{ form.password|as_crispy_field }}
        </div>
      </div>
            {{ form.address_1|as_crispy_field }}
            {{ form.address_2|as_crispy_field }}
      <div class="form-row">
        <div class="form-group col-md-6 mb-0">
          {{ form.city|as_crispy_field }}
        </div>
        <div class="form-group col-md-4 mb-0">
          {{ form.state|as_crispy_field }}
        </div>
        <div class="form-group col-md-2 mb-0">
          {{ form.zip_code|as_crispy_field }}
        </div>
      </div>
      {{ form.check_me_out|as_crispy_field }}
      <button type="submit" class="btn btn-primary">Sign in</button>
   -->
"""