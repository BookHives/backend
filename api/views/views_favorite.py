from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from ..models import FavoritePages, User, Book
from ..serializers import FavoritePagesSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_user_favorites(request, user_id):
    """Get all favorites for a user with optional status filter"""
    try:
        status_filter = request.GET.get('status')
        
        # Use direct integer field instead of foreign key
        favorites = FavoritePages.objects.filter(user_id=user_id)
        
        if status_filter:
            favorites = favorites.filter(reading_status=status_filter)
        
        serializer = FavoritePagesSerializer(favorites, many=True)
        
        # Add additional debug logging
        logger.info(f"Found {favorites.count()} favorites for user {user_id}")
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching favorites for user {user_id}: {str(e)}")
        return Response(
            {'error': f'Failed to fetch favorites: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def add_favorite(request):
    """Add a book to favorites"""
    try:
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        reading_status = request.data.get('reading_status', 'WANT_TO_READ')

        # Check if favorite already exists
        favorite, created = FavoritePage.objects.get_or_create(
            user_id=user_id,
            book_id=book_id,
            defaults={'reading_status': reading_status}
        )

        if not created:
            return Response(
                {'error': 'Book is already in favorites'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FavoritePageSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response(
            {'error': 'Invalid user_id or book_id'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        logger.error(f"Error adding favorite: {str(e)}")
        return Response(
            {'error': 'Failed to add favorite'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['PUT'])
def update_reading_status(request):
    """Update reading status of a favorite book"""
    try:
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        new_status = request.data.get('reading_status')

        favorite = get_object_or_404(
            FavoritePage, 
            user_id=user_id, 
            book_id=book_id
        )
        
        favorite.reading_status = new_status
        favorite.save()
        
        serializer = FavoritePageSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error updating reading status: {str(e)}")
        return Response(
            {'error': 'Failed to update reading status'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['DELETE'])
def remove_favorite(request, user_id, book_id):
    """Remove a book from favorites"""
    try:
        favorite = get_object_or_404(
            FavoritePage, 
            user_id=user_id, 
            book_id=book_id
        )
        favorite.delete()
        
        return Response(
            {'message': 'Book removed from favorites'}, 
            status=status.HTTP_200_OK
        )

    except Exception as e:
        logger.error(f"Error removing favorite: {str(e)}")
        return Response(
            {'error': 'Failed to remove favorite'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_reading_status_books(request, user_id, reading_status):
    """Get all books with a specific reading status"""
    try:
        favorites = FavoritePage.objects.filter(
            user_id=user_id,
            reading_status=reading_status
        )
        serializer = FavoritePageSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error fetching reading status books: {str(e)}")
        return Response(
            {'error': 'Failed to fetch books'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )