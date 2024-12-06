import os
import django
from datetime import datetime
from django.db import connection

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CST438.settings')
django.setup()

def execute_sql(query, params=None):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query, params)
            print(f"Successfully executed: {query[:100]}...")
        except Exception as e:
            print(f"Error executing query: {query[:100]}...")
            print(f"Error message: {str(e)}")

def populate_database():
    # Clear existing data (optional)
    clear_queries = [
        "DELETE FROM favorite_page;",
        "DELETE FROM review;",
        "DELETE FROM book;",
        "DELETE FROM user;"
    ]

    print("Clearing existing data...")
    for query in clear_queries:
        execute_sql(query)

    # Add users (including librarian)
    user_queries = [
        """
        INSERT INTO user (username, email, password, is_librarian, created_at)
        VALUES ('john_doe', 'john@example.com', 'password123', 0, NOW());
        """,
        """
        INSERT INTO user (username, email, password, is_librarian, created_at)
        VALUES ('jane_smith', 'jane@example.com', 'password123', 0, NOW());
        """,
        """
        INSERT INTO user (username, email, password, is_librarian, created_at)
        VALUES ('admin_lib', 'admin@library.com', 'admin123', 1, NOW());
        """
    ]

    # Add books
    book_queries = [
        """
        INSERT INTO book (title, author, description, genre, published_date, available_copies, created_at, updated_at)
        VALUES (
            'The Great Gatsby',
            'F. Scott Fitzgerald',
            'A story of decadence and excess.',
            'FICTION',
            '1925-04-10',
            3,
            NOW(),
            NOW()
        );
        """,
        """
        INSERT INTO book (title, author, description, genre, published_date, available_copies, created_at, updated_at)
        VALUES (
            '1984',
            'George Orwell',
            'A dystopian novel.',
            'FICTION',
            '1949-06-08',
            2,
            NOW(),
            NOW()
        );
        """,
        """
        INSERT INTO book (title, author, description, genre, published_date, available_copies, created_at, updated_at)
        VALUES (
            'Pride and Prejudice',
            'Jane Austen',
            'A romantic novel of manners.',
            'FICTION',
            '1813-01-28',
            5,
            NOW(),
            NOW()
        );
        """
    ]

    # Add reviews
    review_queries = [
        """
        INSERT INTO review (user_id, book_id, rating, review_text, created_at, updated_at)
        SELECT 
            (SELECT user_id FROM user WHERE username = 'john_doe'),
            (SELECT book_id FROM book WHERE title = 'The Great Gatsby'),
            5,
            'A masterpiece of American literature!',
            NOW(),
            NOW();
        """,
        """
        INSERT INTO review (user_id, book_id, rating, review_text, created_at, updated_at)
        SELECT 
            (SELECT user_id FROM user WHERE username = 'jane_smith'),
            (SELECT book_id FROM book WHERE title = '1984'),
            4,
            'A chilling and thought-provoking read.',
            NOW(),
            NOW();
        """
    ]

    # Add favorite pages with different reading statuses
    favorite_queries = [
        """
        INSERT INTO favorite_pages (user_id, book_id, reading_status, created_at)
        SELECT 
            (SELECT user_id FROM user WHERE username = 'john_doe'),
            (SELECT book_id FROM book WHERE title = 'The Great Gatsby'),
            'CURRENTLY_READING',
            NOW();
        """,
        """
        INSERT INTO favorite_pages (user_id, book_id, reading_status, created_at)
        SELECT 
            (SELECT user_id FROM user WHERE username = 'john_doe'),
            (SELECT book_id FROM book WHERE title = '1984'),
            'WANT_TO_READ',
            NOW();
        """,
        """
        INSERT INTO favorite_pages (user_id, book_id, reading_status, created_at)
        SELECT 
            (SELECT user_id FROM user WHERE username = 'jane_smith'),
            (SELECT book_id FROM book WHERE title = 'Pride and Prejudice'),
            'ALREADY_READ',
            NOW();
        """
    ]

    print("\nAdding users...")
    for query in user_queries:
        execute_sql(query)

    print("\nAdding books...")
    for query in book_queries:
        execute_sql(query)

    print("\nAdding reviews...")
    for query in review_queries:
        execute_sql(query)

    print("\nAdding favorites...")
    for query in favorite_queries:
        execute_sql(query)

def verify_data():
    verification_queries = {
        "Users": "SELECT user_id, username, is_librarian FROM user",
        "Books": "SELECT book_id, title, author FROM book",
        "Reviews": """
            SELECT r.review_id, u.username, b.title, r.rating, r.comment 
            FROM review r 
            JOIN user u ON r.user_id = u.user_id 
            JOIN book b ON r.book_id = b.book_id
        """,
        "Favorites": """
            SELECT f.favorite_id, u.username, b.title, f.reading_status 
            FROM favorite_page f 
            JOIN user u ON f.user_id = u.user_id 
            JOIN book b ON f.book_id = b.book_id
        """
    }

    print("\nVerifying data:")
    for table_name, query in verification_queries.items():
        print(f"\n{table_name}:")
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)

if __name__ == "__main__":
    print("Starting database population...")
    populate_database()
    print("\nVerifying populated data...")
    verify_data()