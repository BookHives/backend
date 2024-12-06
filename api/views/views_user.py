from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import User
from ..serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def api_root(request):
    """Root endpoint showing all available API endpoints"""
    return Response({
        'message': 'Welcome to BookHive API',
        'endpoints': {
            'users': {
                'all_users': '/api/users/',
                'login': '/api/users/login/',
                'logout': '/api/users/logout/',
                'update': '/api/users/update/',
                'delete': '/api/users/delete/'
            },
            'books': {
                'all_books': '/api/books/',
                'book_detail': '/api/books/<id>/',
                'create_book': '/api/books/create/',
                'add_review': '/api/books/<id>/review/'
            },
            'favorites': {
                'add_favorite': '/api/books/favorite/',
                'get_favorites': '/api/users/<id>/favorites/'
            }
        }
    })

@api_view(['GET'])
def get_all_users(request):
    """Get all users in the database"""
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # Only return necessary user information for security
        safe_data = [{
            'user_id': user['user_id'],
            'username': user['username'],
            'is_librarian': user['is_librarian']
        } for user in serializer.data]
        return Response(safe_data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return Response(
            {'error': 'Failed to fetch users'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def login(request):
    """Handle user login"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Username and password are required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = get_object_or_404(User, username=username)
        
        # In production, use proper password hashing
        if user.password == password:  # Replace with proper password verification
            serializer = UserSerializer(user)
            return Response({
                'message': 'Login successful',
                'user': {
                    'user_id': user.user_id,
                    'username': user.username,
                    'is_librarian': user.is_librarian
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Invalid credentials'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return Response(
            {'error': 'Login failed'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )

@api_view(['POST'])
def logout(request):
    """Handle user logout"""
    user_id = request.data.get('user_id')
    try:
        user = get_object_or_404(User, pk=user_id)
        return Response(
            {'message': 'Logout successful'}, 
            status=status.HTTP_200_OK
        )
    except Exception as e:
        logger.error(f"Logout error: {str(e)}")
        return Response(
            {'error': 'Logout failed'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['DELETE'])
def delete_account(request):
    """Delete user account"""
    user_id = request.data.get('user_id')
    password = request.data.get('password')
    
    try:
        user = get_object_or_404(User, pk=user_id)
        
        # Verify password before deletion
        if user.password == password:  # Replace with proper password verification
            user.delete()
            return Response(
                {'message': 'Account deleted successfully'}, 
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Invalid password'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
    except Exception as e:
        logger.error(f"Account deletion error: {str(e)}")
        return Response(
            {'error': 'Failed to delete account'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['PUT'])
def update_user(request):
    """Update user settings"""
    user_id = request.data.get('user_id')
    current_password = request.data.get('current_password')
    
    try:
        user = get_object_or_404(User, pk=user_id)
        
        # Verify current password
        if user.password != current_password:  # Replace with proper password verification
            return Response(
                {'error': 'Invalid current password'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Update fields if provided
        if 'new_username' in request.data:
            # Check if username is already taken
            if User.objects.filter(username=request.data['new_username']).exclude(pk=user_id).exists():
                return Response(
                    {'error': 'Username already taken'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.username = request.data['new_username']
            
        if 'new_email' in request.data:
            user.email = request.data['new_email']
            
        if 'new_password' in request.data:
            user.password = request.data['new_password']  # Use proper password hashing
            
        if 'profile_image' in request.data:
            user.profile_image = request.data['profile_image']
        
        user.save()
        return Response(
            {'message': 'Profile updated successfully'}, 
            status=status.HTTP_200_OK
        )
            
    except Exception as e:
        logger.error(f"Profile update error: {str(e)}")
        return Response(
            {'error': 'Failed to update profile'}, 
            status=status.HTTP_400_BAD_REQUEST
        )