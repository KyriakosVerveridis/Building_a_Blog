from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
	"""
	Tag model represents a blog tag.
	"""
	caption = models.CharField(max_length=20) # Post's caption

	def __str__(self):
		return self.caption # String representation of the Tag object


class Author(models.Model):
	"""
	Author model represents a blog author.
	"""
	first_name = models.CharField(max_length=100) # Author's first name
	last_name = models.CharField(max_length=100) # Author's last name
	email_address = models.EmailField()	# Author's email address

	def full_name(self):
		return f"{self.first_name} {self.last_name}"

	def __str__(self):
		return self.full_name() # String representation of the Author object


class Post(models.Model):
	"""
	Post model represents a blog post.
	"""
	title = models.CharField(max_length=150) # Title of the post
	excerpt = models.CharField(max_length=200) # Short summary or excerpt (optional)
	image = models.ImageField(upload_to="posts", null=True) # Stores an uploaded image for each post.
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
	




    
	
    

	

