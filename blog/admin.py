from django.contrib import admin
from .models import Post
# we are importing the post model we defined in models.py

admin.site.register(Post)
# registering the model makes it visible on the page
