# movies_update_and_delete.py
# Name: Noor Al Salihi
# Assignment: Module 8 – Movies Update and Delete

import mysql.connector


# ---------------------------------------------------
# Function to display selected fields from film table
# ---------------------------------------------------
def show_films(cursor, title):
    print("\n-- {} --".format(title))

    query = """
        SELECT 
            film.film_name AS Name,
            film.film_director AS Director,
            genre.genre_name AS Genre,
            studio.studio_name AS Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """

    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(
            film[0], film[1], film[2], film[3]
        ))


# ---------------------------------------------------
# Connect to the database
# ---------------------------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Noor1998$$$$",   # Your password
    database="movies"
)

cursor = db.cursor()


# ---------------------------------------------------
# 1. Display initial films
# ---------------------------------------------------
show_films(cursor, "DISPLAYING FILMS BEFORE CHANGES")


# ---------------------------------------------------
# 2. INSERT a new film
# (Added film_releaseDate to match your table structure)
# ---------------------------------------------------
insert_query = """
    INSERT INTO film (film_name, film_director, studio_id, genre_id, film_runtime, film_releaseDate)
    VALUES ('Inception', 'Christopher Nolan', 1, 2, 148, '2010')
"""
cursor.execute(insert_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


# ---------------------------------------------------
# 3. UPDATE Alien → Horror (genre_id = 1)
# ---------------------------------------------------
update_query = """
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
"""
cursor.execute(update_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")


# ---------------------------------------------------
# 4. DELETE Gladiator
# ---------------------------------------------------
delete_query = """
    DELETE FROM film
    WHERE film_name = 'Gladiator'
"""
cursor.execute(delete_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


# ---------------------------------------------------
# Close the connection
# ---------------------------------------------------
db.close()
