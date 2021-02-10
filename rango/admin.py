from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulate_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
