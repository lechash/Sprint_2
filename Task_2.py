class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'


comedy_collection = Comedy()
drama_collection = Drama()

result_comedy = comedy_collection.add_movie('Большой куш')
print(result_comedy)


result_drama = drama_collection.add_movie('Оружейный барон')
print(result_drama)