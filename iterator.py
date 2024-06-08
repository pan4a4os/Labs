class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def __repr__(self):
        return f"'{self.title}' directed by {self.director}"

class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def __iter__(self):
        return CinemaIterator(self.movies)

class CinemaIterator:
    def __init__(self, movies):
        self._movies = movies
        self._index = 0

    def __next__(self):
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        else:
            raise StopIteration

    def __iter__(self):
        return self

cinema = Cinema()
cinema.add_movie(Movie("Inception", "Christopher Nolan"))
cinema.add_movie(Movie("The Matrix", "Lana and Lilly Wachowski"))
cinema.add_movie(Movie("Parasite", "Bong Joon-ho"))

for movie in cinema:
    print(movie)
