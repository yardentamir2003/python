import re

from chapter14.Q2 import actor
from chapter14.Q2.actor import Actor


def main():
    actors_list = []
    while True:
        option = input(
            "1. List actors by age\n2. Add actor\n3. Delete actor\n4. Delete movie\n5. Quit\nChoose option: ")
        if valid_option(option):
            if option == "1":
                option_one(actors_list)
                continue
            if option == "2":
                option_two(actors_list)
                continue
            if option == "3":
                option_three(actors_list)
                continue
            if option == "4":
                option_four(actors_list)
                continue
            if option == "5":
                print("OK, have a good one!")
                break
            else:
                print("Invalid input, please enter 1/2/3/4/5")


def valid_option(option):
    match = re.findall('^[12345]$', option)
    if len(match) == 0:
        return False
    return True


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


def option_one(actors_list):
    if len(actors_list) == 0:
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
    for actor in actors_list:
        if actor.is_in_age_range(from_age, to_age):
            zero_match = False
            movies_number = len(actor.movies)
            print("{}, ({} movies).".format(actor.name, movies_number))
    if zero_match:
        print("Can't find actors in this age range.")


def option_two(actors_list):
    actor_name = input("Enter the actor’s name: ")
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

    actors_list.append(actor)


def option_three(actors_list):
    while True:
        if len(actors_list) == 0:
            print("The actors list is empty. Can't delete actors.")
        deleted_actor = input("Enter actor name: ")
        for actor in actors_list:
            if deleted_actor == actor.name:
                actors_list.remove(actor)
                print("OK, the actor {} was deleted".format(deleted_actor))
                return
        print("{} doesn't exist in the actors list.".format(deleted_actor))


def option_four(actors_list):
    if len(actors_list) == 0:
        print("Actors list is empty.")
        return
    movie_name = input("Enter movie name: ")
    affected_actors = 0
    for actor in actors_list:
        if actor.is_in_movie(movie_name):
            delete_movie(actors_list, movie_name)
            affected_actors += 1
    if affected_actors == 0:
        print("The movie doesn't exist.")
    elif affected_actors == 1:
        print(
            "OK, the movie {} was deleted, 1 actor was affected by this change.".format(movie_name))
    else:
        print(
            "OK, the movie {} was deleted, {} actors were affected by this change.".format(movie_name, affected_actors))


def delete_movie(actors_list, movie_name):
    for actor in actors_list:
        for movie in actor.movies:
            if movie == movie_name:
                actor.movies.remove(movie_name)


main()
