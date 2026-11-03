class Human:
    def perform(self):
        print("Moving to a scene")

class Singer(Human):
    def perform(self):
        super().perform()
        print("Singing....")

class Guitarist(Human):
    def perform(self):
        super().perform()
        print("Playing guitar....")

class Artist(Singer, Guitarist):
    def perform(self):
        super().perform()


artist = Artist()

artist.perform()

print(
    Artist.mro()
)

class Artist:
    def perform(self):
        print("Творить мистецтво.")


class Singer(Artist):
    def perform(self):
        super().perform()
        print("Співає пісню.")


class Guitarist(Artist):
    def perform(self):
        super().perform()
        print("Грає соло на гітарі.")


# Множинне успадкування
class RockStar(Singer, Guitarist):
    def perform(self):
        print("=== Початок шоу ===")
        super().perform()


# --- Використання ---

star = RockStar()
star.perform()