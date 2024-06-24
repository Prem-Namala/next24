from tkinter import *
from lyricsgenius import Genius

genius = Genius("YOUR_ACCESS_TOKEN_HERE")

def extract_lyrics():
    song = song_entry.get()
    artist = artist_entry.get()

    try:
        song = genius.search_song(song, artist)
        lyrics = song.lyrics
        lyrics_text.delete(1.0, END)
        lyrics_text.insert(END, lyrics)
    except Exception as e:
        print(e)
        lyrics_text.delete(1.0,  END)
        lyrics_text.insert( END, "Error: Could not find lyrics.")

window =  Tk()
window.title("Lyrics Extractor")
window.geometry("600x500")

Label(window, text="").grid(row = 0)

Label(window, text="Song", padx = 5).grid(row = 1, sticky = 'e')
song_entry = Entry(window)
song_entry.grid(row = 1, column = 1, sticky = 'w')

Label(window, text="").grid(row = 2)

Label(window, text="Artist", padx = 5).grid(row=3, sticky = 'e')
artist_entry = Entry(window)
artist_entry.grid(row = 3, column = 1, sticky = 'w')

Label(window, text="").grid(row = 4)

Button(window, text="Extract Lyrics", command=extract_lyrics).grid(row=5, column=0, columnspan=2)

Label(window, text="").grid(row = 6)
Label(window, text="").grid(row = 7)

lyrics_text = Text(window, padx = 20, width = 70)
lyrics_text.grid(row = 8, column = 0, columnspan = 2, sticky = 'nsew')

window.mainloop()