from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('title',)
    list_display_links = ('title',)
    list_editable = ('content',)
    list_per_page = 5

admin.site.register(Article, ArticleAdmin)