from big_princess import BigPrincess
from princess import Princess


def main():
    snow_white = Princess("snow white")
    ariel = Princess("Ariel")
    ariel.hello()
    snow_white.hello()
    ariel.hello()
    snow_white.hello()
    snow_white.hello()

    abuela = BigPrincess("abuela")
    abuela.jump()
    abuela.hello()
    abuela.jump()
    abuela.jump()
    abuela.jump()
    abuela.jump()


main()
