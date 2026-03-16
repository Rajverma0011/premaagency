from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tiles/", views.catalog, name="catalog"),
    path("tile/<int:id>/", views.tile_detail, name="tile_detail"),
    path("category/<str:category>/", views.category_tiles, name="category_tiles"),
    path("contact/", views.contact, name="contact"),
    path("sanitary/", views.sanitary_page, name="sanitary"),

path("sanitary/<str:category>/", views.sanitary_category, name="sanitary_category"),
path("sanitary/product/<int:id>/", views.sanitary_detail, name="sanitary_detail"),
]