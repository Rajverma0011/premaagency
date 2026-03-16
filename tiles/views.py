from django.shortcuts import render, get_object_or_404
from .models import Tile , Sanitary


def home(request):
    return render(request, "home.html")


def catalog(request):
    return render(request, "catalog.html")

    if category:
        tiles = Tile.objects.filter(category=category)
    else:
        tiles = Tile.objects.all()

    return render(request, "catalog.html", {"tiles": tiles})


def tile_detail(request, id):
    tile = get_object_or_404(Tile, id=id)
    return render(request, "tile_detail.html", {"tile": tile})
def category_tiles(request, category):

    tiles = Tile.objects.filter(category=category)

    return render(request, "category_tiles.html", {
        "tiles": tiles,
        "category": category
    })
def contact(request):
    return render(request, "contact.html")
from .models import ContactMessage

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, "contact.html")
def sanitary_page(request):
    sanitary_items = Sanitary.objects.all()
    return render(request, "sanitary.html", {"items": sanitary_items})


def sanitary_category(request, category):
    items = Sanitary.objects.filter(category=category)

    return render(request, "sanitary_category.html", {
        "items": items,
        "category": category
    })
from .models import Sanitary
from django.shortcuts import get_object_or_404

def sanitary_detail(request, id):

    product = get_object_or_404(Sanitary, id=id)

    return render(request, "sanitary_detail.html", {
        "product": product
    })
