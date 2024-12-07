from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ..models import Book, User, Review, FavoritePages
from ..serializers import BookSerializer, ReviewSerializer, FavoritePagesSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_all_books(request):
    """Get all books for homepage display"""
    try:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching books: {str(e)}")
        return Response(
            {'error': 'Failed to fetch books'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_book_detail(request, book_id):
    """Get detailed information about a specific book"""
    try:
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        
        # Get book reviews
        reviews = Review.objects.filter(book_id=book_id)
        review_serializer = ReviewSerializer(reviews, many=True)
        
        response_data = {
            'book': serializer.data,
            'reviews': review_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching book details: {str(e)}")
        return Response(
            {'error': 'Failed to fetch book details'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['POST'])
def add_to_favorites(request):
    """Add a book to user's favorites"""
    try:
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        reading_status = request.data.get('reading_status', 'WANT_TO_READ')
        
        # Validate user and book exist
        user = get_object_or_404(User, pk=user_id)
        book = get_object_or_404(Book, pk=book_id)
        
        # Add to favorites with reading status
        favorite, created = FavoritePages.objects.get_or_create(
            user_id=user,
            book_id=book,
            defaults={'reading_status': reading_status}
        )
        
        if not created:
            return Response(
                {'error': 'Book is already in favorites'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = FavoritePagesSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(f"Error adding book to favorites: {str(e)}")
        return Response(
            {'error': 'Failed to add book to favorites'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def create_book(request):
    """Create a new book (librarian only)"""
    user_id = request.data.get('user_id')
    
    try:
        # Check if user is a librarian
        user = get_object_or_404(User, pk=user_id)
        if not user.is_librarian:
            return Response(
                {'error': 'Only librarians can create books'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Create new book
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        logger.error(f"Error creating book: {str(e)}")
        return Response(
            {'error': 'Failed to create book'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def create_review(request, book_id):
    """Create a review for a book"""
    try:
        # Validate book exists
        book = get_object_or_404(Book, pk=book_id)
        
        # Create review
        review_data = {
            'user': request.data.get('user_id'),
            'book': book_id,
            'rating': request.data.get('rating'),
            'review_text': request.data.get('review_text')  # Changed from comment to review_text
        }
        
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        logger.error(f"Error creating review: {str(e)}")
        return Response(
            {'error': 'Failed to create review'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def search_books(request):
    """Search books by title, author, or genre"""
    query = request.GET.get('q', '')
    try:
        books = Book.objects.filter(
            Q(genre__icontains=query)
        )
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error searching books: {str(e)}")
        return Response(
            {'error': 'Failed to search books'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )