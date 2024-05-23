import pickle

class Song:
    def __init__(self, title, artist, album, year):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.artist} from the album '{self.album}' released in {self.year}"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                print(f"Removed: {song}")
                return
        print(f"Song '{title}' not found in the playlist.")

    def list_songs(self):
        if not self.songs:
            print("The playlist is empty.")
        else:
            for song in self.songs:
                print(song)

    def find_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                print(song)
                return
        print(f"Song '{title}' not found in the playlist.")

    def sort_songs_by_title(self):
        self.songs.sort(key=lambda song: song.title)
        print("Songs sorted by title.")

    def sort_songs_by_artist(self):
        self.songs.sort(key=lambda song: song.artist)
        print("Songs sorted by artist.")

    def play_next(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)
            print(f"Playing: {self.songs[self.current_index]}")
        else:
            print("The playlist is empty.")

    def play_previous(self):
        if self.songs:
            self.current_index = (self.current_index - 1) % len(self.songs)
            print(f"Playing: {self.songs[self.current_index]}")
        else:
            print("The playlist is empty.")

    def play_current(self):
        if self.songs:
            print(f"Playing: {self.songs[self.current_index]}")
        else:
            print("The playlist is empty.")


class PlaylistManager:
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name):
        if name in self.playlists:
            print(f"Playlist '{name}' already exists.")
        else:
            self.playlists[name] = Playlist(name)
            print(f"Created playlist '{name}'.")

    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
            print(f"Deleted playlist '{name}'.")
        else:
            print(f"Playlist '{name}' not found.")

    def list_playlists(self):
        if not self.playlists:
            print("No playlists available.")
        else:
            for name in self.playlists:
                print(name)

    def find_playlist(self, name):
        return self.playlists.get(name, None)

    def search_by_artist(self, artist):
        found = False
        for playlist in self.playlists.values():
            for song in playlist.songs:
                if song.artist.lower() == artist.lower():
                    print(song)
                    found = True
        if not found:
            print(f"No songs found by artist '{artist}'.")


def save_playlists(manager, filename):
    with open(filename, 'wb') as f:
        pickle.dump(manager, f)
    print(f"Playlists saved to {filename}.")

def load_playlists(filename):
    try:
        with open(filename, 'rb') as f:
            manager = pickle.load(f)
        print(f"Playlists loaded from {filename}.")
        return manager
    except FileNotFoundError:
        print(f"No file found with name {filename}.")
        return PlaylistManager()


def main():
    manager = PlaylistManager()

    while True:
        print("\nMusic Playlist Application")
        print("1. Create a playlist")
        print("2. Delete a playlist")
        print("3. List all playlists")
        print("4. Add a song to a playlist")
        print("5. Remove a song from a playlist")
        print("6. List all songs in a playlist")
        print("7. Find a song in a playlist")
        print("8. Search for songs by artist")
        print("9. Sort songs in a playlist by title")
        print("10. Sort songs in a playlist by artist")
        print("11. Play next song")
        print("12. Play previous song")
        print("13. Play current song")
        print("14. Save playlists to file")
        print("15. Load playlists from file")
        print("16. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the playlist name: ")
            manager.create_playlist(name)

        elif choice == '2':
            name = input("Enter the playlist name to delete: ")
            manager.delete_playlist(name)

        elif choice == '3':
            print("\nPlaylists:")
            manager.list_playlists()

        elif choice == '4':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                title = input("Enter the song title: ")
                artist = input("Enter the artist: ")
                album = input("Enter the album: ")
                year = input("Enter the year: ")
                song = Song(title, artist, album, year)
                playlist.add_song(song)
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '5':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                title = input("Enter the song title to remove: ")
                playlist.remove_song(title)
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '6':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                print(f"\nSongs in playlist '{playlist_name}':")
                playlist.list_songs()
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '7':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                title = input("Enter the song title to find: ")
                playlist.find_song(title)
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '8':
            artist = input("Enter the artist name to search: ")
            manager.search_by_artist(artist)

        elif choice == '9':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                playlist.sort_songs_by_title()
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '10':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                playlist.sort_songs_by_artist()
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '11':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                playlist.play_next()
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '12':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                playlist.play_previous()
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '13':
            playlist_name = input("Enter the playlist name: ")
            playlist = manager.find_playlist(playlist_name)
            if playlist:
                playlist.play_current()
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == '14':
            filename = input("Enter the filename to save playlists: ")
            save_playlists(manager, filename)

        elif choice == '15':
            filename = input("Enter the filename to load playlists: ")
            manager = load_playlists(filename)

        elif choice == '16':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
