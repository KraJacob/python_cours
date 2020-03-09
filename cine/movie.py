import json
import os
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR,"data","movies.json")


class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE,'r') as f:
            return json.load(f)

    def _write_movie(self, movies):
        with open(DATA_FILE,"w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movie(self):
        movies = self._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            self._write_movie(movies)
            return True
        else:
            logging.warning(f"le filme {self.title} existe déjà dans la base de données.")
            return False

    def remove_from_movie(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movie(movies)
            return True
        else:
            logging.warning(f"le filme {self.title} n'existe pas dans la liste")

    def get_movies(self):
        with open(DATA_FILE,'r') as f:
            movies_title = json.load(f)
        movies = [Movie(movie_title) for movie_title in movies_title]
        return movies
    

if __name__ == "__name__":
    m = Movie("harry potter")
    print(m)
m = Movie("Avengers Endgamme")
print(m.get_movies())