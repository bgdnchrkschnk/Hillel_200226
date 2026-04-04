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