# it takes request as an arugument and return a dict. of data as in context
from .models import Category


def menu_links(request):
    links = Category.objects.all()
    return dict (links=links)