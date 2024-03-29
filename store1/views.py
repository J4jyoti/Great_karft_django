
from django.shortcuts import render, get_object_or_404
from .models import Product
from store.models import Category

# Create your views here.
def store1(request,category_slug= None):
    print("--->",category_slug)
    categories = None
    products = None
    context = {} 

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)        
        product_count = products.count() 
        print("--->>",product_count)


    else:
        products = Product.objects.all().filter()
        
    product_count = products.count()

    context =({

        'products': products,
        'product_count': product_count,
       
        })
        

    return render(request,'store1/store.html', context)



def product_detail(request, category_slug, product_slug ):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context= {
        'single_product': single_product,
    }
    return render(request, 'store1/product_detail.html', context)


    
