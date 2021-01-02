from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #    'title': obj.title,
    #    'description': obj.description,
    #    'price': obj.price,
    #    'summary': obj.summary,
    #    'featured': obj.featured,
    # }
    context = {
        'object': obj
    }
    # return render(request, 'product/detail.html', context)
    return render(request, 'products/product_detail.html', context)


def product_create_view(request):  # this is for the raw HTML example? shortcut version of the one done there
    form = ProductForm(request.POST or None)  # have the form as the class needed, instantiate the class
    if form.is_valid():            # checks if its valid..?
        form.save()                # save the form
        form = ProductForm()       # new form once the thing saved on the website. re render the form

    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)


"""
def product_create_view(request): #django form, makes the HTML stuff easier, long version of the one above?
    # my_form = RawProductForm() # creates instance of the form. doesn't get any data and save it, bc POST isnt captured
    # making the form work the long way. First display the form in line below, then once filled and POST request, boom
    my_form = RawProductForm()  # argument is Request.GET automatically, so can leave it
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)      # validates things. makes the field required
        if my_form.is_valid(): # if the form hasn't been tampered with
            # now the data is good
            print(my_form.cleaned_data)  # getting clean data
            # print(my_form)
            # can also save data, as shown:
            Product.objects.create(**my_form.cleaned_data) # saving data to the database
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }

    return render(request, 'products/product_create.html', context)

"""
# def product_create_view(request): #was for a random explanation on HTML working. Not necessarily the form
    # print(request.GET)       #  prints the GET query on the website
    # print(request.POST)      #  prints the POST query ting on the website

    # can use request.GET to save data but its wrong and insecure
    # use POST to save to the stuff.

    # if request.Method == 'POST':   # if a POST as been used, get the contents and save it to the database
    #     my_new_title = request.POST.get('title')      # getting the title from the POST
    #     print(my_new_title)                # printing it
    #     Product.objects.create(title=my_new_title) #storing it

    # this method is more secure, uses RAW HTML form, but is a bad and clunky way of doing it.
    # does not validate if the data is clean

    # context = {}

    # return render(request, 'products/product_create.html', context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'object': obj
    }
    return render(request, 'products/product_create.html', context)


def render_initial_data(request):
    # having the form show up with data already there
    initial_data = {
        'title': 'My Awesome Title'
    }
    # form = ProductForm(request.POST or None, initial=initial_data)

    # editing something in the database manually - getting it then saving
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)


# Dynamic URL routing, ie changing the url yourself
def dynamic_lookup_view(request, my_id):
    # changing content based on the URL
    # obj = Product.objects.get(id=my_id)    # won't work if the object id doesn't exist
    # obj = get_object_or_404(Product, id=my_id)  # solves the problem, gives a 404 error if not found

    # can do it in a try block, preferred up ting bc its quicker
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # Post Request
    if request.method == 'POST':
        # confirming delete, not method to delete
        obj.delete()
        return redirect('./products')
    context = {
        'object': obj
    }

    return render(request, 'products/product_delete.html', context)


def product_list_view(request):  # essentially printing the things out as a list
    queryset = Product.objects.all()  # gets all the objects as a query set (use queryset to make this app reusable)
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)
