from .models import Category, User

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)