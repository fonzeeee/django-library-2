from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(choices=(
        (1, "Available"),
        (2, "Checked Out"),
        (3, "Damaged"),
        (4, "Lost"),
    ), default=1)
    type = models.PositiveSmallIntegerField(choices=(
        (1, "Hardcover"),
        (2, "Paperback"),
        (3, "Digital Copy"),
    ), default=1),
    location = models.PositiveSmallIntegerField(choices=(
        (1, "Exactus Office"),
        (2, "Owner's Home"),
        (3, "In the Matrix"),
    ), default=1)
    #authors = ambot unsaon??
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=100)
    #author = FK to Users - Author is Logged In User
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content