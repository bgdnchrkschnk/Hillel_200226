class TestFailedError(Exception):
    pass


class Song:
    def __init__(self, name: str, artist: str, bpm: int, duration: float):
        self.name = name
        self.__artist = artist
        self.__bpm = bpm
        self.__duration = duration

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


eminem_8_mile: Song = Song("8 mile", "Eminem", 120, 5.30)

name = eminem_8_mile.name
artist = eminem_8_mile.artist
bpm = eminem_8_mile.bpm
duration = eminem_8_mile.duration

new_duration_value = 3
eminem_8_mile.duration = new_duration_value

# assert eminem_8_mile.duration == 3, f"Duration value is not equal to {new_duration_value}"

# positive test
assert getattr(eminem_8_mile, "duration") == 3, f"Duration value is not equal to {new_duration_value}"

# negative test
try:
    new_duration_value = 7
    setattr(eminem_8_mile, "duration", new_duration_value)
# except ValueError:
#     print("Test passed, error is catched")
except Exception as e:
    if isinstance(e, ValueError):
        print("Test passed, error is catched")
    else:
        raise TestFailedError(f"Test failed, actual error is not value error")