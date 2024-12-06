# serializers.py
from rest_framework import serializers
from .models import User, Book, Review, FavoritePages

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class FavoritePagesSerializer(serializers.ModelSerializer):
    book_details = serializers.SerializerMethodField()
    
    class Meta:
        model = FavoritePages
        fields = ['favorite_id', 'user_id', 'book_id', 'reading_status', 'created_at', 'book_details']
    
    def get_book_details(self, obj):
        try:
            book = Book.objects.get(book_id=obj.book_id)
            return {
                'title': book.title,
                'author': book.author,
                'genre': book.genre
            }
        except Book.DoesNotExist:
            return None