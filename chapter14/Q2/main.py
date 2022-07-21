import re
from actor import Actor


def main():
    actors_list = []
    while True:
        option = input("1. List actors by age\n2. Add actor\n3. Delete actor\n4. Delete movie\n5. Quit\nChoose option: ")
        if valid_option(option):
            # if option == "1":
            #     option_one()
            if option == "2":
                option_two(actors_list)
                continue
            if option == "3":
                option_three(actors_list)
                continue
            # if option == "4":
            #     option_four()
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


def option_two(actors_list):
    actor_name = input("Enter the actor’s name: ")
    while True:
        actor_birth_year = input("Enter the actor’s birth year: ")
        if valid_birth_year(actor_birth_year):
            break
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
    # actor.is_in_age_range()


def option_three(actors_list):
    while True:
        deleted_actor = input("Enter actor name: ")
        if deleted_actor in actors_list:
            break
        else:
            print("{} doesn't exist in the actors list.".format(deleted_actor))
    print("OK, the actor {} was deleted".format(deleted_actor))




def valid_birth_year(actor_birth_year):
    match = re.findall('^\d{4}$', actor_birth_year)
    if len(match) == 0:
        return False
    return True

main()