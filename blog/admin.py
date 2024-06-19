from django.contrib import admin
from .models import Article, Author
from django.contrib import messages


@admin.action(description='make published articles')
def make_article_published(self, request, queryset):
    updated = queryset.update(worthiness='GOLD')
    self.message_user(request, f'{updated} is published', messages.SUCCESS)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'worthiness', 'updated_date']
    search_fields = ['title', 'text']
    list_filter = ['author', 'worthiness']
    empty_value_display = 'No Data Available'
    list_editable = ['worthiness']
    date_hierarchy = 'updated_date'
    ordering = ['worthiness']
    fieldsets = [
        ('Article Info', {
            'fields': [
                'title', 'text', 'image', 'categories'
            ],
        }),
        (
            'Author Info', {
                'fields': ['author'],
                'classes': ['collapse']
            }
        )
    ]
    raw_id_fields = ['author']
    prepopulated_fields = {'text': ['title']}
    actions = [make_article_published]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'level']