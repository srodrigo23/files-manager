import eyed3





audio=eyed3.load("media/05. Ferxxo 100.mp3")
print("Title:",audio.tag.title)
print("Artist:",audio.tag.artist)
print("Album:",audio.tag.album)
print("Album artist:",audio.tag.album_artist)
print("Composer:",audio.tag.composer)
print("Publisher:",audio.tag.publisher)