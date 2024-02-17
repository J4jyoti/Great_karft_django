from django.shortcuts import render
from store1.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all().filter()

    context = {
        'products': products,
    }
    return render(request, 'home.html', context )


