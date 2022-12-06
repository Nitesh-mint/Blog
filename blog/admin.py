from django.contrib import admin
from .models import Post

class AdminView(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on','category')
    list_filter = ("status",)
    search_fields = ['title','content','category']
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Post, AdminView)

