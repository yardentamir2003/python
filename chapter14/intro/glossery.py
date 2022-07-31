# class, the name of the class starts with a capital letter.
class Actor:
    # constractor, the "__init__" function, where the instance of the class is created.
    def __init__(self, name, birth_year, movies):
        self.name = name
        self.birth_year = birth_year
        self.movies = movies

    # method1, the functions in the class.
    def is_in_age_range(self, from_age, to_age):
        birth_year = int(self.birth_year)
        age = datetime.datetime.now().year - birth_year
        if from_age <= age <= to_age:
            return True
        return False

    # method2 the functions in the class.
    def is_in_movie(self, move_name):
        for movie in self.movies:
            if movie == move_name:
                return True
        return False


# Usually, in the "main" file we create the instance of the class and send it's parameters (in case of need).
# for example:
# actor = Actor(actor_name, actor_birth_year, movies)