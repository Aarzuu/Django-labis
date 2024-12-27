from django.contrib import admin

from .models import CreateForum



class CreateForumAdmin(admin.ModelAdmin):
    fields = ["title", "description", "author", "pub_date"]
    list_display = ["title", "description", "author", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["title", "author"]

admin.site.register(CreateForum, CreateForumAdmin)
