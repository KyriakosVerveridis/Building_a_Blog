from django.contrib import admin
from .models import Tag, Author, Post, Comment

# Register your models here.


# Register the Tag model
@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
  	list_display = ("caption",)


# Register the Author model
@admin.register(Author)
class AuhorAdmin(admin.ModelAdmin):
  	list_display = ("full_name",)


# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_filter= ("author", "author", "tags",)
	list_display = ("title", "date", "author",)
	prepopulated_fields = {"slug":("title",)}


# Register the Comment model
@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
  	list_display = ("user_name", "post",)		
	