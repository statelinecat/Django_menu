from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    fields = ('title', 'parent', 'order', 'url', 'named_url')
    extra = 1
    show_change_link = True

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'order', 'get_resolved_url')
    list_filter = ('menu',)
    search_fields = ('title', 'url', 'named_url')
    ordering = ('menu', 'parent', 'order')

    def get_resolved_url(self, obj):
        return obj.get_url()
    get_resolved_url.short_description = 'URL'
