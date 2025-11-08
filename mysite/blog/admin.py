from django.contrib import admin
from .models import Tag,Author,Post

# Register your models here.


# Register the Tag model
@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
  list_display = ("caption",)


# Register the Author model
@admin.register(Author)
class AuhorAdmin(admin.ModelAdmin):
  list_display = ("first_name","last_name","email_address",)


# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("title","excerpt","image_name","date","slug","content",)