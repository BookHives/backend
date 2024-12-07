from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Review, Book, User
from ..serializers import ReviewSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_book_reviews(request, book_id):
    """Get all reviews for a specific book"""
    try:
        reviews = Review.objects.filter(book_id=book_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching reviews for book {book_id}: {str(e)}")
        return Response(
            {'error': 'Failed to fetch reviews'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_user_reviews(request, user_id):
    """Get all reviews by a specific user"""
    try:
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching reviews for user {user_id}: {str(e)}")
        return Response(
            {'error': 'Failed to fetch user reviews'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def create_review(request):
    """Create a new review"""
    try:
        data = {
            'user_id': request.data.get('user_id'),
            'book_id': request.data.get('book_id'),
            'rating': request.data.get('rating'),
            'review_text': request.data.get('review_text'),
        }
        
        # Check if user has already reviewed this book
        existing_review = Review.objects.filter(
            user_id=data['user_id'],
            book_id=data['book_id']
        ).exists()
        
        if existing_review:
            return Response(
                {'error': 'You have already reviewed this book'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create the review
        review = Review.objects.create(**data)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['PUT'])
def update_review(request, review_id):
    """Update an existing review"""
    try:
        review = get_object_or_404(Review, pk=review_id)
        
        # Verify the user owns this review
        if review.user_id != request.data.get('user_id'):
            return Response(
                {'error': 'You can only edit your own reviews'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        logger.error(f"Error updating review {review_id}: {str(e)}")
        return Response(
            {'error': 'Failed to update review'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['DELETE'])
def delete_review(request, review_id):
    """Delete a review"""
    try:
        review = get_object_or_404(Review, pk=review_id)
        
        # Verify the user owns this review
        if review.user_id != request.data.get('user_id'):
            return Response(
                {'error': 'You can only delete your own reviews'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        review.delete()
        return Response(
            {'message': 'Review deleted successfully'}, 
            status=status.HTTP_200_OK
        )
        
    except Exception as e:
        logger.error(f"Error deleting review {review_id}: {str(e)}")
        return Response(
            {'error': 'Failed to delete review'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )