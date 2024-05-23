# Music Playlist Application

A console-based music playlist application to efficiently manage and organize songs.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Classes and Functionalities](#classes-and-functionalities)
- [Authors](#authors)

## Features
- Create, edit, and delete playlists
- Add and remove songs from playlists
- Search for songs by title or artist
- Sort songs by title or artist
- Playback controls (play next, previous, and current song)
- Save and load playlists to/from files

## Usage

1. **Create a Playlist:**
    - Select the option to create a new playlist and provide a name.
2. **Add a Song:**
    - Choose a playlist and enter the song details (title, artist, album, year).
3. **Remove a Song:**
    - Select a playlist and provide the title of the song to remove.
4. **List Songs:**
    - List all songs in a selected playlist.
5. **Search for Songs by Artist:**
    - Enter the artist's name to find all songs by that artist.
6. **Sort Songs:**
    - Sort the songs in a playlist by title or artist.
7. **Playback Controls:**
    - Navigate through songs in the playlist using play next, previous, or current song options.
8. **Save and Load Playlists:**
    - Save the current state of playlists to a file and load them later.

## Classes and Functionalities

| Class            | Attributes                                         | Methods                                                             | Description                                                                                 |
|------------------|----------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `Song`           | `title`, `artist`, `album`, `year`                 | `__init__`, `__str__`                                               | Represents a song with a title, artist, album, and release year.                            |
| `Playlist`       | `name`, `songs`, `current_index`                   | `add_song`, `remove_song`, `list_songs`, `find_song`, `sort_songs_by_title`, `sort_songs_by_artist`, `play_next`, `play_previous`, `play_current` | Manages a collection of songs, including adding, removing, listing, finding, sorting, and playback controls. |
| `PlaylistManager`| `playlists`                                        | `create_playlist`, `delete_playlist`, `list_playlists`, `find_playlist`, `search_by_artist` | Manages multiple playlists, including creating, deleting, listing, finding playlists, and searching for songs by artist. |

### Song Class
- **Attributes:**
  - `title`: The title of the song.
  - `artist`: The artist of the song.
  - `album`: The album the song belongs to.
  - `year`: The year the song was released.
- **Methods:**
  - `__init__(title, artist, album, year)`: Initializes a new Song object.
  - `__str__()`: Returns a string representation of the Song object.

### Playlist Class
- **Attributes:**
  - `name`: The name of the playlist.
  - `songs`: A list of Song objects.
  - `current_index`: An index to track the currently playing song.
- **Methods:**
  - `add_song(song)`: Adds a Song object to the playlist.
  - `remove_song(title)`: Removes a Song object from the playlist by title.
  - `list_songs()`: Lists all songs in the playlist.
  - `find_song(title)`: Finds and prints a song by title.
  - `sort_songs_by_title()`: Sorts the songs by their title.
  - `sort_songs_by_artist()`: Sorts the songs by their artist.
  - `play_next()`: Plays the next song in the playlist.
  - `play_previous()`: Plays the previous song in the playlist.
  - `play_current()`: Plays the current song.

### PlaylistManager Class
- **Attributes:**
  - `playlists`: A dictionary of Playlist objects.
- **Methods:**
  - `create_playlist(name)`: Creates a new playlist.
  - `delete_playlist(name)`: Deletes a playlist by name.
  - `list_playlists()`: Lists all available playlists.
  - `find_playlist(name)`: Finds and returns a Playlist object by name.
  - `search_by_artist(artist)`: Searches for songs by a specific artist across all playlists.

## Authors

- [Joel Xhelili](https://github.com/joelxh22)
