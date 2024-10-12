from django.db import models

class Artists(models.Model):
    """
    To store information about Artists
    """

    name = models.CharField(max_length=200)
    profile = models.TextField()
    date_of_birth = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lyricists(models.Model):
    """
    To store information about Lyricists
    """

    name = models.CharField(max_length=200)
    profile = models.TextField()
    date_of_birth = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    """
    To store information about music
    """

    title =  models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    album_name = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artists, related_name= "music_artists")
    composed_by = models.ManyToManyField(Artists, related_name="music_compositions")
    lyricist = models.ForeignKey(Lyricists, related_name="lyrics_writer", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class MusicReview(models.Model):
    """
    Stores the information of music reviews
    """

    music = models.ForeignKey(Music, related_name="music_review", on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return "Review of " + self.music.title
