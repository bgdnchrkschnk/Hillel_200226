class TestFailedError(Exception):
    pass


class Song:
    __total_songs = 0

    def __init__(self, name: str, artist: str, bpm: int, duration: float):
        self.name = name
        self.__artist = artist
        self.__bpm = bpm
        self.__duration = duration
        self.__class__.__total_songs += 1
        # Song.total_songs += 1

    @property
    def artist(self):
        return self.__artist

    @property
    def bpm(self):
        return self.__bpm

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_duration_value):
        if (new_duration_value < 0.3) or (new_duration_value > 10):
            raise ValueError(f"Song duration must be between 0.3 and 10 minutes")
        self.__duration = new_duration_value


    def __str__(self):
        format = f"Artist name is {self.__artist}, song name is {self.name} " \
                 f"rhytm is {self.__bpm} and duration is {self.__duration} minutes"
        return format


    @classmethod
    def get_total_songs(cls):
        return cls.__total_songs


eminem_8_mile: Song = Song("8 mile", "Eminem", 120, 5.30)

assert Song.get_total_songs() == 1

name = eminem_8_mile.name
artist = eminem_8_mile.artist
bpm = eminem_8_mile.bpm
duration = eminem_8_mile.duration

new_duration_value = 3
eminem_8_mile.duration = new_duration_value

overal_count = Song.get_total_songs()
print(overal_count)