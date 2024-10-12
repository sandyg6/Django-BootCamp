from django.contrib import admin
from music_review_app.models import Artists, Lyricists, Music, MusicReview

admin.site.register(Artists)
admin.site.register(Lyricists)
admin.site.register(Music)
admin.site.register(MusicReview)
