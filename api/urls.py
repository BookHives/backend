from django.urls import path
from .views import views_user, views_book, views_review, views_favorite

urlpatterns = [
    # Root endpoint
    path('', views_user.api_root, name='api-root'),

    # User endpoints
    path('users/', views_user.get_all_users, name='get-all-users'),
    path('users/login/', views_user.login, name='login'),
    path('users/logout/', views_user.logout, name='logout'),
    path('users/delete/', views_user.delete_account, name='delete-account'),
    path('users/update/', views_user.update_user, name='update-user'),

    # Book endpoints
    path('books/', views_book.get_all_books, name='get-all-books'),
    path('books/<int:book_id>/', views_book.get_book_detail, name='get-book-detail'),
    path('books/search/', views_book.search_books, name='search-books'),
    path('books/create/', views_book.create_book, name='create-book'),

    # Review endpoints
    path('books/<int:book_id>/reviews/', views_review.get_book_reviews, name='get-book-reviews'),
    path('users/<int:user_id>/reviews/', views_review.get_user_reviews, name='get-user-reviews'),
    path('reviews/', views_review.create_review, name='create-review'),
    path('reviews/<int:review_id>/', views_review.update_review, name='update-review'),
    path('reviews/<int:review_id>/delete/', views_review.delete_review, name='delete-review'),

    # Favorite endpoints
    path('users/<int:user_id>/favorites/', views_favorite.get_user_favorites, name='get-user-favorites'),
    path('favorites/add/', views_favorite.add_favorite, name='add-favorite'),
    path('favorites/status/update/', views_favorite.update_reading_status, name='update-reading-status'),
    path('favorites/<int:user_id>/<int:book_id>/remove/', views_favorite.remove_favorite, name='remove-favorite'),
    path('users/<int:user_id>/reading/<str:reading_status>/', views_favorite.get_reading_status_books, name='get-reading-status-books'),
]