from django.contrib import admin

from entry.models import Entry, Category


class entryAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Entry, entryAdmin)
admin.site.register(Category, CategoryAdmin)