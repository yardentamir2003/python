import datetime


class Actor:
    def __init__(self, name, birth_year, movies):
        self.name = name
        self.birth_year = birth_year
        self.movies = movies

    def is_in_age_range(self, from_age,to_age):
        birth_year = int(self.birth_year)
        age = datetime.datetime.now().year - birth_year
        print(age)


    # def is_in_movie(self, move_name):