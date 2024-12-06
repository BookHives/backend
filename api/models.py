# models.py
from django.db import models

class User(models.Model):
    class Meta:
        db_table = 'user'
        
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=200)
    is_librarian = models.BooleanField(default=False)
    profile_image = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    class Meta:
        db_table = 'book'
        
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    published_date = models.DateField()
    cover_image = models.CharField(max_length=255, null=True)
    available_copies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    class Meta:
        db_table = 'review'
        
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, db_column='book_id')
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FavoritePages(models.Model):
    class Meta:
        db_table = 'favorite_pages'
        
    favorite_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()  # Changed from ForeignKey to match table structure
    book_id = models.IntegerField()  # Changed from ForeignKey to match table structure
    reading_status = models.CharField(
        max_length=20,
        choices=[
            ('WANT_TO_READ', 'Want to Read'),
            ('CURRENTLY_READING', 'Currently Reading'),
            ('ALREADY_READ', 'Already Read')
        ],
        default='WANT_TO_READ'
    )
    created_at = models.DateTimeField(auto_now_add=True)