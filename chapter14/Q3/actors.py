import re

from chapter14.Q3.actor import Actor


class Actors:
    def __init__(self):
        self.actors_list = []

    def list_by_age(self):
        if len(self.actors_list) == 0:
            print("Actors list is empty.")
            return
        while True:
            age_range = input("Enter actors age range: ")
            if valid_age_range(age_range):
                break
            else:
                print("Please enter age range in format Ddd-Ddd, when d is optional.")
        splitted_age_range = age_range.split("-")
        from_age = int(splitted_age_range[0])
        to_age = int(splitted_age_range[1])
        zero_match = True
        for actor in self.actors_list:
            if actor.is_in_age_range(from_age, to_age):
                zero_match = False
                movies_number = len(actor.movies)
                print("{}, ({} movies).".format(actor.name, movies_number))
        if zero_match:
            print("Can't find actors in this age range.")

    def add_actor(self):
        actor_name = input("Enter the actor’s name: ")
        for actor in self.actors_list:
            if actor_name == actor.name:
                print("The actor {} already exist.".format(actor_name))
                return
        while True:
            actor_birth_year = input("Enter the actor’s birth year: ")
            if valid_birth_year(actor_birth_year):
                break
            else:
                print("Please enter a year in format DDDD.")
        movies = []
        movie_count = 0
        while True:
            movie = input("Enter the actor’s movies, or click Enter to complete: ")
            if movie == "":
                actor = Actor(actor_name, actor_birth_year, movies)
                print("OK, actor {} added, and {} movies specified.".format(actor_name, movie_count))
                break
            else:
                movies.append(movie)
                movie_count += 1

        self.actors_list.append(actor)

    def delete_actor(self):
        while True:
            if len(self.actors_list) == 0:
                print("The actors list is empty. Can't delete actors.")
                return
            deleted_actor = input("Enter actor name: ")
            for actor in self.actors_list:
                if deleted_actor == actor.name:
                    self.actors_list.remove(actor)
                    print("OK, the actor {} was deleted".format(deleted_actor))
                    return
            print("{} doesn't exist in the actors list.".format(deleted_actor))

    def delete_movie(self):
        if len(self.actors_list) == 0:
            print("Actors list is empty.")
            return
        movie_name = input("Enter movie name: ")
        affected_actors = 0
        for actor in self.actors_list:
            if actor.is_in_movie(movie_name):
                affected_actors += 1
                actor.movies.remove(movie_name)
        if affected_actors != 0 and affected_actors != 1:
            print(
                "OK, the movie {} was deleted, {} actors were affected by this change.".format(movie_name,
                                                                                               affected_actors))
        elif affected_actors == 0:
            print("The movie doesn't exist.")
        else:
            print(
                "OK, the movie {} was deleted, 1 actor was affected by this change.".format(movie_name))


def valid_age_range(age_range):
    match = re.findall('^(\d{1,3}-\d{1,3})$', age_range)
    if len(match) == 0:
        return False
    return True


def valid_birth_year(actor_birth_year):
    match = re.findall('^\d{4}$', actor_birth_year)
    if len(match) == 0:
        return False
    return True