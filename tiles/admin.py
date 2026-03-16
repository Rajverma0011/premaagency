from django.contrib import admin
from .models import Tile , Sanitary
from .models import ContactMessage

admin.site.register(ContactMessage)
@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "price", "size")
    list_filter = ("category",)
    search_fields = ("name", "material", "color")
@admin.register(Sanitary)
class SanitaryAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "brand", "price")
    list_filter = ("category", "brand")
    search_fields = ("name", "description")
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")