favorite_movies = [
    {"name": "The Lion King", "year": 1994},
    {"name": "The Matrix", "year": 1999},
    {"name": "Spirited Away", "year": 2001},
    {"name": "Inception", "year": 2010},
    {"name": "Parasite", "year": 2019}
]


def check_movie(movie):
    if movie["year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie.get("name", movie.get("title"))


recent_movies = []

for movie in favorite_movies:
    returned_movie = check_movie(movie)
    if returned_movie is not None:
        recent_movies.append(returned_movie)

print(recent_movies)
