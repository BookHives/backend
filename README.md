# BookHive Backend API - Django REST Framework

## ---

## Overview

BookHive Backend API is a comprehensive Django REST Framework application that serves as the backend infrastructure for the BookHive digital library management system. The API provides secure, scalable endpoints for user authentication, book management, review systems, and personal reading list functionality.

**Live API:** [https://bookhive-90e4e8826675.herokuapp.com/api/](https://bookhive-90e4e8826675.herokuapp.com/api/)

The backend integrates with a MySQL database hosted on JawsDB (Heroku add-on) and provides RESTful API endpoints for:

* User authentication and profile management including Google OAuth integration
* Comprehensive book catalog management with CRUD operations
* Review and rating system with user-generated content
* Personal reading list management with multiple reading statuses
* Administrative functions for librarian users
* Cross-Origin Resource Sharing (CORS) configured for frontend integration

This API serves as the foundation for the BookHive digital library platform, providing robust data management and business logic for efficient library operations and user engagement.

## ---

## Technology Stack

### Core Technologies

* [Django](https://www.djangoproject.com/) - High-level Python web framework
  * [Documentation](https://docs.djangoproject.com/)
  * [Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
  * [GitHub Repository](https://github.com/django/django)
* [Django REST Framework](https://www.django-rest-framework.org/) - Powerful toolkit for building Web APIs
  * [Documentation](https://www.django-rest-framework.org/)
  * [Quickstart Guide](https://www.django-rest-framework.org/tutorial/quickstart/)
  * [GitHub Repository](https://github.com/encode/django-rest-framework)
* [MySQL](https://www.mysql.com/) - Relational database management system
  * [Documentation](https://dev.mysql.com/doc/)
  * [Python MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
* [JawsDB](https://devcenter.heroku.com/articles/jawsdb) - Heroku MySQL add-on
  * [Documentation](https://devcenter.heroku.com/articles/jawsdb)
  * [Configuration Guide](https://devcenter.heroku.com/articles/jawsdb#using-jawsdb-with-django)
* [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX
  * [Documentation](https://docs.gunicorn.org/)
  * [Deployment Guide](https://docs.gunicorn.org/en/stable/deploy.html)

### Supporting Libraries

* [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - CORS handling for Django
* [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
* [whitenoise](https://whitenoise.evans.io/) - Static file serving for Python web apps
* [mysqlclient](https://github.com/PyMySQL/mysqlclient) - MySQL database adapter

### Package Management

* [pip](https://pip.pypa.io/) - Python package installer
  * [Documentation](https://pip.pypa.io/en/stable/)
  * [User Guide](https://pip.pypa.io/en/stable/user_guide/)

## ---

## Workflow & Setup Guide

### Installation and Setup

#### Prerequisites

* Python 3.8 or higher
* pip package manager
* MySQL database (local or remote)
* Virtual environment tool (recommended)

#### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd bookhive-backend
```

#### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv bookhive_env

# Activate virtual environment
# On Windows:
bookhive_env\Scripts\activate
# On macOS/Linux:
source bookhive_env/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Database Configuration (example with JawsDB)
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=3306

# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True

# For production deployment
ALLOWED_HOSTS=localhost,127.0.0.1,bookhive-90e4e8826675.herokuapp.com
```

#### Step 5: Database Setup

```bash
# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Populate with sample data (optional)
python populate_db.py
```

#### Step 6: Test the Setup

```bash
# Test database connection
python test_db.py

# Verify Django setup
python test_setup.py
```

#### Step 7: Start the Development Server

```bash
python manage.py runserver
```

#### Step 8: Access the API

Navigate to [http://localhost:8000/api/](http://localhost:8000/api/) for local development, or visit the live API at [https://bookhive-90e4e8826675.herokuapp.com/api/](https://bookhive-90e4e8826675.herokuapp.com/api/)

## Project Structure

```
bookhive-backend/
├── CST438/                    # Django project configuration
│   ├── __init__.py               # Python package initialization
│   ├── settings.py               # Django settings and configuration
│   ├── urls.py                   # Main URL routing configuration
│   ├── wsgi.py                   # WSGI application for deployment
│   └── asgi.py                   # ASGI application for async support
├── api/                      # Main API application
│   ├── migrations/               # Database migration files
│   │   ├── __init__.py               # Migration package initialization
│   │   └── 0001_initial.py           # Initial database schema migration
│   ├── views/                    # API view modules organized by functionality
│   │   ├── __init__.py               # Views package initialization
│   │   ├── views_user.py             # User authentication and profile endpoints
│   │   ├── views_book.py             # Book management and search endpoints
│   │   ├── views_review.py           # Review and rating system endpoints
│   │   └── views_favorite.py         # Reading list and favorites endpoints
│   ├── __init__.py               # API package initialization
│   ├── admin.py                  # Django admin interface configuration
│   ├── apps.py                   # Django app configuration
│   ├── models.py                 # Database models and schema definitions
│   ├── serializers.py            # Django REST Framework serializers
│   ├── tests.py                  # Unit tests for API functionality
│   └── urls.py                   # API URL routing and endpoint definitions
├── .env                      # Environment variables configuration
├── Procfile                  # Heroku deployment configuration
├── manage.py                 # Django management script
├── requirements.txt          # Python package dependencies
├── populate_db.py            # Database population script with sample data
├── test_db.py                # Database connection testing utility
├── test_setup.py             # Django setup verification script
└── verify_db.py              # Database verification and diagnostics
```

### Key Directories and Files

#### Core Configuration

* **CST438/**: Main Django project directory containing global settings
  * settings.py configures database connections, CORS, middleware, and installed apps
  * urls.py provides the main URL routing that includes API routes
  * wsgi.py serves as the WSGI application entry point for production deployment

#### API Application

* **api/models.py**: Defines database schema and relationships
  * User model with authentication and profile information
  * Book model with comprehensive metadata and availability tracking
  * Review model linking users and books with ratings and text reviews
  * FavoritePages model for reading list management with status tracking

* **api/views/**: Modular view organization by functionality
  * views_user.py handles authentication, login, logout, and profile management
  * views_book.py manages book CRUD operations, search, and discovery
  * views_review.py implements review creation, editing, and deletion
  * views_favorite.py provides reading list management and status updates

#### Database and Deployment

* **migrations/**: Django database migration files for schema management
* **Procfile**: Heroku deployment configuration specifying Gunicorn as the web server
* **requirements.txt**: Python package dependencies with specific versions for reproducible builds

#### Utility Scripts

* **populate_db.py**: Comprehensive database seeding with sample users, books, reviews, and favorites
* **test_db.py**: Database connection diagnostics and table verification
* **verify_db.py**: Environment variable validation and connection testing

## ---

## Database Models and Schema

The API uses a relational database design with four main models:

### User Model

```python
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=200)
    is_librarian = models.BooleanField(default=False)
    profile_image = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Purpose**: Manages user authentication, profiles, and role-based access control

**Key Features**:
* Unique username and email constraints
* Role differentiation between regular users and librarians
* Google OAuth profile image support
* Automatic timestamp tracking for account creation

### Book Model

```python
class Book(models.Model):
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
```

**Purpose**: Stores comprehensive book information and metadata

**Key Features**:
* Complete bibliographic information including title, author, and description
* Genre categorization for filtering and organization
* Cover image URL storage for visual presentation
* Inventory tracking with available copies count
* Automatic timestamp management for creation and updates

### Review Model

```python
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Purpose**: Implements user-generated reviews and ratings system

**Key Features**:
* Foreign key relationships linking users and books
* Numeric rating system (typically 1-5 stars)
* Text-based review content for detailed feedback
* Cascade deletion to maintain data integrity
* Timestamp tracking for review creation and modification

### FavoritePages Model

```python
class FavoritePages(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()
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
```

**Purpose**: Manages personal reading lists with status tracking

**Key Features**:
* Reading status choices for organization (Want to Read, Currently Reading, Already Read)
* Direct integer references to user and book IDs for flexibility
* Default status assignment for new additions
* Creation timestamp for tracking when books were added to lists

## ---

## Critical API Functions

Here are the key functions that provide the core functionality of the BookHive API:

### User Authentication and Management

**views_user.py** - Authentication and profile management

```python
@api_view(['POST'])
def login(request):
    """Handle user login including Google OAuth integration"""
    email = request.data.get('email')
    
    try:
        # Try to get existing user
        user = User.objects.get(email=email)
        
        # Update profile image if provided (from Google)
        if request.data.get('profile_image'):
            user.profile_image = request.data.get('profile_image')
            user.save()
            
    except User.DoesNotExist:
        # Create new user for Google OAuth
        user = User.objects.create(
            username=request.data.get('username'),
            email=email,
            password=request.data.get('password'),
            profile_image=request.data.get('profile_image')
        )
    
    # Return user data with authentication status
    return Response({
        'message': 'Login successful',
        'user': {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'is_librarian': user.is_librarian,
            'profile_image': user.profile_image
        }
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    """Handle user logout and session cleanup"""
    user_id = request.data.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_users(request):
    """Retrieve all users with security filtering"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    # Return only safe user information
    safe_data = [{
        'user_id': user['user_id'],
        'username': user['username'],
        'is_librarian': user['is_librarian']
    } for user in serializer.data]
    return Response(safe_data, status=status.HTTP_200_OK)
```

### Book Management and Discovery

**views_book.py** - Book catalog and search functionality

```python
@api_view(['GET'])
def get_all_books(request):
    """Retrieve all books for library display"""
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
    """Get comprehensive book information including reviews"""
    try:
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        
        # Get associated reviews
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
def create_book(request):
    """Create new book entry (librarian only)"""
    user_id = request.data.get('user_id')
    
    try:
        # Verify librarian privileges
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

@api_view(['GET'])
def search_books(request):
    """Search books by genre with query parameter"""
    query = request.GET.get('q', '')
    try:
        books = Book.objects.filter(Q(genre__icontains=query))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error searching books: {str(e)}")
        return Response(
            {'error': 'Failed to search books'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
```

### Review and Rating System

**views_review.py** - User-generated content management

```python
@api_view(['POST'])
def create_review(request):
    """Create new book review with rating"""
    try:
        data = {
            'user_id': request.data.get('user_id'),
            'book_id': request.data.get('book_id'),
            'rating': request.data.get('rating'),
            'review_text': request.data.get('review_text'),
        }
        
        # Prevent duplicate reviews from same user
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

@api_view(['DELETE'])
def delete_review(request, review_id):
    """Delete review with ownership verification"""
    try:
        review = get_object_or_404(Review, pk=review_id)
        
        # Verify ownership or librarian privileges
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

@api_view(['GET'])
def get_book_reviews(request, book_id):
    """Retrieve all reviews for a specific book"""
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
```

### Reading List and Favorites Management

**views_favorite.py** - Personal reading list functionality

```python
@api_view(['GET'])
def get_user_favorites(request, user_id):
    """Retrieve user's reading list with optional status filtering"""
    try:
        status_filter = request.GET.get('status')
        
        favorites = FavoritePages.objects.filter(user_id=user_id)
        
        if status_filter:
            favorites = favorites.filter(reading_status=status_filter)
        
        serializer = FavoritePagesSerializer(favorites, many=True)
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
    """Add book to user's reading list"""
    try:
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        reading_status = request.data.get('reading_status', 'WANT_TO_READ')

        # Prevent duplicate favorites
        favorite, created = FavoritePages.objects.get_or_create(
            user_id=user_id,
            book_id=book_id,
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
        logger.error(f"Error adding favorite: {str(e)}")
        return Response(
            {'error': 'Failed to add favorite'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['PUT'])
def update_reading_status(request):
    """Update reading status for a favorited book"""
    try:
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        new_status = request.data.get('reading_status')

        favorite = get_object_or_404(
            FavoritePages, 
            user_id=user_id, 
            book_id=book_id
        )
        
        favorite.reading_status = new_status
        favorite.save()
        
        serializer = FavoritePagesSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error updating reading status: {str(e)}")
        return Response(
            {'error': 'Failed to update reading status'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_reading_status_books(request, user_id, reading_status):
    """Get books filtered by specific reading status"""
    try:
        favorites = FavoritePages.objects.filter(
            user_id=user_id,
            reading_status=reading_status
        )
        serializer = FavoritePagesSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error fetching reading status books: {str(e)}")
        return Response(
            {'error': 'Failed to fetch books'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
```

### Serializers for Data Transformation

**serializers.py** - Django REST Framework serializers

```python
class FavoritePagesSerializer(serializers.ModelSerializer):
    book_details = serializers.SerializerMethodField()
    
    class Meta:
        model = FavoritePages
        fields = ['favorite_id', 'user_id', 'book_id', 'reading_status', 'created_at', 'book_details']
    
    def get_book_details(self, obj):
        """Embed book information in favorite responses"""
        try:
            book = Book.objects.get(book_id=obj.book_id)
            return {
                'title': book.title,
                'author': book.author,
                'genre': book.genre,
                'cover_image': book.cover_image
            }
        except Book.DoesNotExist:
            return None
```

## ---

## API Endpoints Documentation

The BookHive API provides comprehensive endpoints organized by functionality:

### Base URL
* **Production**: `https://bookhive-90e4e8826675.herokuapp.com/api/`
* **Development**: `http://localhost:8000/api/`

### User Authentication Endpoints

#### Root API Information
```
GET /api/
```
Returns API overview and available endpoints

#### User Management
```
GET /api/users/
POST /api/users/login/
POST /api/users/logout/
PUT /api/users/update/
DELETE /api/users/delete/
```

**Login Request Example**:
```json
{
    "username": "user@example.com",
    "email": "user@example.com",
    "password": "google_oauth_token",
    "profile_image": "https://example.com/profile.jpg"
}
```

**Login Response Example**:
```json
{
    "message": "Login successful",
    "user": {
        "user_id": 1,
        "username": "user",
        "email": "user@example.com",
        "is_librarian": false,
        "profile_image": "https://example.com/profile.jpg"
    }
}
```

### Book Management Endpoints

#### Book Operations
```
GET /api/books/                     # Get all books
GET /api/books/<book_id>/           # Get specific book with reviews
GET /api/books/search/?q=<query>    # Search books by genre
POST /api/books/create/             # Create new book (librarian only)
```

**Book Creation Request Example**:
```json
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "description": "A story of decadence and excess in the Jazz Age",
    "genre": "Classic",
    "published_date": "1925-04-10",
    "cover_image": "https://example.com/gatsby.jpg",
    "available_copies": 3,
    "user_id": 1
}
```

**Book Detail Response Example**:
```json
{
    "book": {
        "book_id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A story of decadence and excess in the Jazz Age",
        "genre": "Classic",
        "published_date": "1925-04-10",
        "cover_image": "https://example.com/gatsby.jpg",
        "available_copies": 3,
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-01-01T10:00:00Z"
    },
    "reviews": [
        {
            "review_id": 1,
            "user": 1,
            "book": 1,
            "rating": 5,
            "review_text": "A masterpiece of American literature!",
            "created_at": "2024-01-02T14:30:00Z"
        }
    ]
}
```

### Review System Endpoints

#### Review Operations
```
GET /api/books/<book_id>/reviews/    # Get reviews for specific book
GET /api/users/<user_id>/reviews/    # Get reviews by specific user
POST /api/reviews/                   # Create new review
PUT /api/reviews/<review_id>/        # Update existing review
DELETE /api/reviews/<review_id>/delete/ # Delete review
```

**Review Creation Request Example**:
```json
{
    "user_id": 1,
    "book_id": 1,
    "rating": 5,
    "review_text": "An absolutely captivating read that explores themes of wealth, love, and the American Dream."
}
```

**Review Response Example**:
```json
{
    "review_id": 1,
    "user": 1,
    "book": 1,
    "rating": 5,
    "review_text": "An absolutely captivating read that explores themes of wealth, love, and the American Dream.",
    "created_at": "2024-01-02T14:30:00Z",
    "updated_at": "2024-01-02T14:30:00Z"
}
```

### Favorites and Reading List Endpoints

#### Reading List Management
```
GET /api/users/<user_id>/favorites/                    # Get all user favorites
GET /api/users/<user_id>/reading/<reading_status>/     # Get books by reading status
POST /api/favorites/add/                               # Add book to favorites
PUT /api/favorites/status/update/                      # Update reading status
DELETE /api/favorites/<user_id>/<book_id>/remove/      # Remove from favorites
```

**Add to Favorites Request Example**:
```json
{
    "user_id": 1,
    "book_id": 1,
    "reading_status": "WANT_TO_READ"
}
```

**Favorites Response Example**:
```json
[
    {
        "favorite_id": 1,
        "user_id": 1,
        "book_id": 1,
        "reading_status": "CURRENTLY_READING",
        "created_at": "2024-01-01T12:00:00Z",
        "book_details": {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Classic",
            "cover_image": "https://example.com/gatsby.jpg"
        }
    }
]
```

**Reading Status Options**:
* `WANT_TO_READ` - Books the user intends to read
* `CURRENTLY_READING` - Books the user is actively reading
* `ALREADY_READ` - Books the user has completed

### Error Response Format

All endpoints return consistent error responses:

```json
{
    "error": "Description of the error that occurred"
}
```

**Common HTTP Status Codes**:
* `200 OK` - Successful operation
* `201 Created` - Resource created successfully
* `400 Bad Request` - Invalid request data
* `401 Unauthorized` - Authentication required
* `403 Forbidden` - Insufficient permissions
* `404 Not Found` - Resource not found
* `500 Internal Server Error` - Server error

## ---

## Database Configuration and Management

### JawsDB MySQL Integration

The API uses JawsDB, a Heroku add-on that provides managed MySQL hosting:

**Connection Configuration** (from settings.py):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```

### Database Management Commands

**Migration Management**:
```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Reset migrations (caution: data loss)
python manage.py migrate api zero
```

**Data Management**:
```bash
# Populate database with sample data
python populate_db.py

# Test database connection
python test_db.py

# Verify environment configuration
python verify_db.py

# Django shell for manual database operations
python manage.py shell
```

### Sample Data Population

The `populate_db.py` script provides comprehensive sample data:

```python
def populate_database():
    # Sample users including librarian
    users_data = [
        {
            'username': 'john_doe',
            'email': 'john@example.com',
            'password': 'password123',
            'is_librarian': False
        },
        {
            'username': 'admin_lib',
            'email': 'admin@library.com',
            'password': 'admin123',
            'is_librarian': True
        }
    ]
    
    # Sample books with metadata
    books_data = [
        {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'description': 'A story of decadence and excess.',
            'genre': 'Classic',
            'published_date': '1925-04-10',
            'available_copies': 3
        }
    ]
    
    # Sample reviews linking users and books
    # Sample favorites with different reading statuses
```

## ---

## Deployment Configuration

### Heroku Deployment

The API is deployed on Heroku at: [https://bookhive-90e4e8826675.herokuapp.com/api/](https://bookhive-90e4e8826675.herokuapp.com/api/)

### Production Configuration

**Procfile Configuration**:
```
web: gunicorn CST438.wsgi
```

**Settings for Production** (settings.py):
```python
# Allowed hosts for production
ALLOWED_HOSTS = [
    'bookhive-90e4e8826675.herokuapp.com',
    'https://bookhive-frontend-1d36e543d26f.herokuapp.com',
    'localhost',
    '127.0.0.1'
]

# CORS configuration for frontend integration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://bookhive-frontend-1d36e543d26f.herokuapp.com",
    "https://bookhive-90e4e8826675.herokuapp.com"
]

# Security middleware stack
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Environment Variables for Production

Required environment variables on Heroku:

```bash
# Database configuration (automatically set by JawsDB)
DB_NAME=your_jawsdb_database_name
DB_USER=your_jawsdb_username
DB_PASSWORD=your_jawsdb_password
DB_HOST=your_jawsdb_host
DB_PORT=3306

# Django configuration
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=bookhive-90e4e8826675.herokuapp.com
```

### Deployment Commands

**Initial Deployment**:
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create bookhive-backend-api

# Add JawsDB MySQL add-on
heroku addons:create jawsdb:kitefin

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy application
git push heroku main

# Run migrations on production
heroku run python manage.py migrate

# Populate production database
heroku run python populate_db.py
```

**Ongoing Deployment**:
```bash
# Deploy changes
git push heroku main

# Run new migrations
heroku run python manage.py migrate

# View logs
heroku logs --tail

# Open production app
heroku open
```

## ---

## Security and Authentication

### CORS Configuration

Cross-Origin Resource Sharing is configured to allow requests from the frontend:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Development frontend
    "https://bookhive-frontend-1d36e543d26f.herokuapp.com",  # Production frontend
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_CREDENTIALS = True
```

### Role-Based Access Control

The API implements role-based permissions:

**Librarian Privileges**:
* Create new books in the catalog
* Delete any user reviews
* Access administrative functions

**Regular User Privileges**:
* Create and manage personal reviews
* Manage personal reading lists
* View all public content

**Permission Checking Example**:
```python
def create_book(request):
    user_id = request.data.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    
    if not user.is_librarian:
        return Response(
            {'error': 'Only librarians can create books'}, 
            status=status.HTTP_403_FORBIDDEN
        )
```

### Data Validation and Security

**Input Validation**:
* Django REST Framework serializers provide automatic data validation
* Custom validation for business logic (e.g., preventing duplicate reviews)
* SQL injection prevention through Django ORM
* XSS protection through proper data serialization

**Error Handling**:
* Comprehensive exception handling in all API endpoints
* Detailed logging for debugging while protecting sensitive information
* Consistent error response format across all endpoints

## ---

## Testing and Quality Assurance

### Database Testing Utilities

**Connection Testing** (test_db.py):
```python
def test_connection():
    """Comprehensive database diagnostics"""
    # Environment variable verification
    # Django settings validation
    # Database connection testing
    # Table structure verification
    # Sample data validation
```

**Setup Verification** (test_setup.py):
```python
def test_django_setup():
    """Django configuration validation"""
    # Django setup verification
    # Installed apps checking
    # Migration status review
    # Database connectivity testing
```

### Recommended Testing Strategies

**Unit Testing**:
```python
# Test model functionality
def test_user_creation():
    user = User.objects.create(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    assert user.username == 'testuser'
    assert not user.is_librarian  # Default value

# Test API endpoints
def test_book_creation_endpoint():
    response = self.client.post('/api/books/create/', {
        'title': 'Test Book',
        'author': 'Test Author',
        'user_id': self.librarian_user.user_id
    })
    assert response.status_code == 201
```

**Integration Testing**:
* Test complete workflows (user registration → book search → review creation)
* Verify CORS functionality with frontend integration
* Test database transactions and rollbacks
* Validate error handling across all endpoints

**Performance Testing**:
* Load testing for concurrent user scenarios
* Database query optimization verification
* API response time monitoring
* Memory usage profiling

## ---

## Contributing

This Django REST Framework API follows industry best practices and welcomes contributions from developers experienced in Python web development.

### Development Guidelines

**Code Organization**:
* Follow Django project structure conventions
* Separate concerns with modular view organization
* Implement proper error handling and logging
* Use Django REST Framework serializers for data transformation

**Database Best Practices**:
* Use Django migrations for all schema changes
* Implement proper foreign key relationships
* Add database indexes for performance optimization
* Use Django ORM instead of raw SQL queries

**API Design Standards**:
* Follow RESTful API conventions
* Implement consistent error response formats
* Use appropriate HTTP status codes
* Provide comprehensive API documentation

### Code Quality Standards

**Python Standards**:
* Follow PEP 8 style guidelines
* Use type hints where appropriate
* Implement comprehensive docstrings
* Use virtual environments for dependency isolation

**Django Conventions**:
* Use Django's built-in authentication and permissions
* Implement proper model validation
* Use Django forms or DRF serializers for data validation
* Follow Django security best practices

**Testing Requirements**:
* Write unit tests for all models and views
* Implement integration tests for API workflows
* Test error conditions and edge cases
* Use Django's testing framework and fixtures

## Next Steps for Future Development

### Enhanced Features

**1. Advanced Authentication and Security**
* JSON Web Token (JWT) implementation for stateless authentication
* OAuth2 integration with multiple providers (GitHub, Facebook, Twitter)
* Two-factor authentication for enhanced security
* Rate limiting to prevent API abuse
* API key management for third-party integrations

**2. Enhanced Search and Filtering**
* Full-text search across book titles, authors, and descriptions
* Advanced filtering with multiple criteria (publication year, rating ranges)
* Search result ranking and relevance scoring
* Autocomplete suggestions for search queries
* Saved searches and search history

**3. Advanced Book Management**
* ISBN lookup integration with external book databases
* Bulk import functionality for large book collections
* Book series and edition management
* Digital book file storage and delivery
* Inventory tracking with detailed availability status

### Performance and Scalability

**1. Database Optimization**
* Query optimization with database indexes
* Database connection pooling for improved performance
* Read replica configuration for scaling read operations
* Database partitioning for large datasets
* Caching layer implementation with Redis

**2. API Performance**
* Pagination for large result sets
* Data caching with Django cache framework
* Asynchronous task processing with Celery
* API response compression
* CDN integration for static content delivery

**3. Monitoring and Analytics**
* Application performance monitoring (APM)
* Error tracking and alerting systems
* Usage analytics and reporting
* API endpoint performance metrics
* Database query performance monitoring

### Integration Capabilities

**1. External API Integration**
* Google Books API for book metadata enrichment
* Goodreads API for additional reviews and ratings
* Library of Congress API for authoritative book information
* Publisher APIs for new release notifications
* Social media APIs for book sharing functionality

**2. Third-Party Services**
* Email service integration for notifications
* SMS service for due date reminders
* Payment processing for book purchases or late fees
* Cloud storage integration for book file management
* Search engine optimization (SEO) improvements

**3. Educational Platform Integration**
* Learning Management System (LMS) connectivity
* School library catalog synchronization
* Reading assignment tracking
* Academic citation format generation
* Integration with reference management tools

### Administrative and Analytics Features

**1. Enhanced Administrative Tools**
* User activity monitoring and analytics
* Content moderation dashboard for reviews
* Bulk user management operations
* System health monitoring and diagnostics
* Automated backup and recovery systems

**2. Reporting and Analytics**
* Popular books and trending analysis
* User engagement and retention metrics
* Review sentiment analysis
* Library usage patterns and statistics
* Custom report generation capabilities

**3. Business Intelligence**
* Recommendation engine based on user behavior
* Predictive analytics for book popularity
* User segmentation and personalization
* A/B testing framework for feature optimization
* Data export capabilities for external analysis

### Mobile and Modern Features

**1. Mobile API Enhancements**
* GraphQL API implementation for flexible mobile queries
* Real-time notifications with WebSocket support
* Offline capability with data synchronization
* Mobile-optimized image processing and delivery
* Push notification service integration

**2. Modern Web Features**
* Server-Sent Events (SSE) for real-time updates
* Progressive Web App (PWA) API support
* WebRTC integration for virtual book clubs
* Machine learning APIs for content recommendations
* Natural language processing for review analysis

This comprehensive backend API provides a robust foundation for the BookHive digital library management system while offering extensive opportunities for future enhancement and scalability. The Django REST Framework architecture ensures maintainable, secure, and performant API services that can grow with the platform's needs.
