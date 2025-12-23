import sqlite3

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER
    )
""")
    conn.commit()

def add_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)   
    VALUES (?, ?, ?, ?, ?, ?)
    """,
                 (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    create_table(conn)
    add_books(conn, "Harry P.", "Rowling", 1997, "Fantasy", 223, 10)
    add_books(conn, "1984", "George Orwell", 1949, "Dystopia", 328, 5)
    add_books(conn, "The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fairy Tale", 96, 8)
    add_books(conn, "The Shining", "Stephen King", 1977, "Horror", 447, 2)
    add_books(conn, "The Martian", "Andy Weir", 2011, "Science Fiction", 369, 4)
    add_books(conn, "Sherlock Holmes", "Arthur Conan Doyle", 1892, "Detective", 307, 5)
    add_books(conn, "The Road", "Cormac McCarthy", 2006, "Post-apocalyptic", 287, 3)
    add_books(conn, "Dracula", "Bram Stoker", 1897, "Gothic Horror", 418, 3)
    add_books(conn, "A Brief History of Time", "Stephen Hawking", 1988, "Popular Science", 212, 4)
    add_books(conn, "Dune", "Frank Herbert", 1965, "Epic Science Fiction", 412, 4)

    conn.close()