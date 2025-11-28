# movies_queries.py
# Name: Noor Al Salihi
# Assignment: Module 7.2 - Movies Table Queries

import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Noor1998$$$$",   # replace with your actual MySQL password
    database="movies"
)

cursor = db.cursor()

# -------------------------------
# Query 1: Display all fields from studio table
# -------------------------------
print("\n-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


# -------------------------------
# Query 2: Display all fields from genre table
# -------------------------------
print("\n-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))


# -------------------------------
# Query 3: Movies with runtime less than 2 hours (120 minutes)
# -------------------------------
print("\n-- DISPLAYING Short Film RECORDS (runtime < 120) --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_films = cursor.fetchall()
for film in short_films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))


# -------------------------------
# Query 4: List of film names and directors grouped by director
# -------------------------------
print("\n-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director")
directors = cursor.fetchall()
for movie in directors:
    print("Director: {}\nFilm Name: {}\n".format(movie[0], movie[1]))

db.close()
