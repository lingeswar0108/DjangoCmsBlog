from django.contrib import admin
from .models import posts,Contact

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','intro', 'is_published','created_date')
    list_filter = ("is_published",)
    search_fields = ['title', 'intro']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(posts,BlogAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject')
admin.site.register(Contact,ContactAdmin)