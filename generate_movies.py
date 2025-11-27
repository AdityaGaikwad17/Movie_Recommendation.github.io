#!/usr/bin/env python3
"""
generate_movies.py

Generates a CSV and JSON file of movies (id, title, year, genre, rating, description).

Usage:
    python generate_movies.py              # generates 1000 movies, outputs movies_with_descriptions.csv/json
    python generate_movies.py 500          # generates 500 movies
    python generate_movies.py 1200 out.csv out.json
"""

import csv
import json
import random
import sys
import os

TITLES = [
    "The Shawshank Redemption","The Godfather","The Dark Knight","Pulp Fiction",
    "Inception","Fight Club","Forrest Gump","The Matrix","Goodfellas","Se7en",
    "Interstellar","Parasite","The Silence of the Lambs","The Green Mile",
    "Gladiator","Saving Private Ryan","The Prestige","The Departed","Whiplash",
    "The Lion King","Titanic","Avatar","The Avengers","Jurassic Park",
    "Back to the Future","Toy Story","Spirited Away","The Terminator",
    "Rocky","Braveheart","The Wolf of Wall Street","Django Unchained",
    "Mad Max: Fury Road","La La Land","The Social Network","The Truman Show",
    "A Beautiful Mind","Black Panther","Iron Man","The Batman","Joker",
    "Shutter Island","The Pianist","Casablanca","2001: A Space Odyssey",
    "Star Wars","The Lord of the Rings","Harry Potter and the Sorcerer's Stone",
    "Indiana Jones and the Last Crusade","Good Will Hunting","The Grand Budapest Hotel",
    "Her","Moonlight","The Big Lebowski","No Country for Old Men","Slumdog Millionaire"
]

GENRES = [
    "Action","Drama","Sci-Fi","Crime","Romance",
    "Thriller","Animation","Comedy","Horror","Adventure"
]

DESCRIPTIONS = [
    "A gripping story filled with emotion and depth.",
    "An unforgettable journey of courage and discovery.",
    "A thrilling adventure that keeps you on the edge.",
    "A powerful drama exploring human relationships.",
    "A visually stunning film with a heartfelt narrative.",
    "A suspenseful ride packed with unexpected twists.",
    "A warm and inspiring tale of hope and resilience.",
    "A fast-paced story with intense action sequences.",
    "A beautifully crafted film with memorable characters.",
    "An emotional story that leaves a lasting impact."
]

def random_year():
    return random.randint(1950, 2024)

def random_rating():
    # rating between 6.5 and 9.8, one decimal
    return round(random.uniform(6.5, 9.8), 1)

def generate_movies(count):
    movies = []
    # If you want more unique titles, you can expand TITLES list or load from a file.
    for i in range(1, count + 1):
        title = random.choice(TITLES)
        year = random_year()
        genre = random.choice(GENRES)
        rating = random_rating()
        description = random.choice(DESCRIPTIONS)
        movies.append({
            "id": i,
            "title": title,
            "year": year,
            "genre": genre,
            "rating": rating,
            "description": description
        })
    return movies

def save_csv(movies, path):
    keys = ["id", "title", "year", "genre", "rating", "description"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for m in movies:
            writer.writerow(m)

def save_json(movies, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)

def main(argv):
    # defaults
    count = 1000
    csv_name = "movies_with_descriptions.csv"
    json_name = "movies.json"

    if len(argv) >= 2:
        try:
            count = int(argv[1])
        except ValueError:
            print("Warning: first argument must be an integer (count). Using default 1000.")
    if len(argv) >= 3:
        csv_name = argv[2]
    if len(argv) >= 4:
        json_name = argv[3]

    out_dir = os.getcwd()  # current directory
    csv_path = os.path.join(out_dir, csv_name)
    json_path = os.path.join(out_dir, json_name)

    movies = generate_movies(count)
    save_csv(movies, csv_path)
    save_json(movies, json_path)

    print(f"Wrote {len(movies)} movies →\n  CSV: {csv_path}\n  JSON: {json_path}")

if __name__ == "__main__":
    main(sys.argv)
