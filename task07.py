class Media:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice
    
    def play(self):
        return f"{self.name} ni {self.voice}formatda eshitayapsiz!"
    
class Song(Media):
    pass

class Movie(Media):
    pass

class Podcast(Media):
    pass

r = Song("Music", "mp3")
r1 = Movie("Kino", "mp4")
r2 = Podcast("Podcast", "mp4a")

print(r.play())
print(r1.play())
print(r2.play())