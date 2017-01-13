from django.db import models
from django.utils import timezone


class Post(models.Model):
    # a class should always begin with capital letter
    author = models.ForeignKey('auth.User')
    # foreignkey is a link to anothe rmodel
    title = models.CharField(max_length=200)
    # charfield defines text with limited number of chars
    text = models.TextField()
    # text field is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    # datetimefield is just what it sounds like
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # def means this is a function or method and publish is its name
        # methods should use lower case and underscores
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # calling __str__() will return a string with a post title
        return self.title
