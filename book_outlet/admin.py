from django.contrib import admin

# Register your models here.
from .models import book, Author, Address, Country

class bookAdmin(admin.ModelAdmin):
    
    prepopulated_fields= {"slug": ("title",)}
    list_filter= ("rating","author",)
    list_display=("title","author",)



admin.site.register(book, bookAdmin) 
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
