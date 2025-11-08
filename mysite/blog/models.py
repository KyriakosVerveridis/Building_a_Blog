from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
	"""
	Tag model represents a blog tag.
	"""
	caption = models.CharField(max_length=20) # Post's caption


class Author(models.Model):
	"""
	Author model represents a blog author.
	"""
	first_name = models.CharField(max_length=100) # Author's first name
	last_name = models.CharField(max_length=100) # Author's last name
	email_address = models.EmailField()	# Author's email address


class Post(models.Model):
	"""
	Post model represents a blog post.
	"""
	title = models.CharField(max_length=150) # Title of the post
	excerpt = models.CharField(max_length=200) # Short summary or excerpt (optional)
	image_name = models.CharField(max_length=100) # Name of the image associated with the post
	date = models.DateField(auto_now=True) # Last modification date, automatically updated
	slug = models.SlugField(unique=True, db_index=True) # URL-friendly unique identifier
	content = models.TextField(validators=[MinLengthValidator(10)]) # Full post content
	author = models.ForeignKey(
    Author,
    on_delete=models.SET_NULL,
    null=True,
    related_name="posts"
)  # Author of this post (relationship)
	tags = models.ManyToManyField(Tag)
	




    
	
    

	

