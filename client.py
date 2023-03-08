import requests
import playlist_2


class Playlist_api:
    def __init__(self, name):
        self.__playlist = playlist_2.Playlist()
        self.__name = name
        self.__playing = False

        # Чтение всех песен по названию плейлиста с сервера
        songs = self.read_song().json()
        # Добавление прочитанных песен в обьект плейлиста
        for song in songs:
            self.add_song(song[0], song[2])

    def play(self):
        """воспроизведение песни в плейлисте"""
        if not self.__playing:
            self.__playlist.play_song()
        else:
            self.__playlist.play()
        self.__playing = True

    def pause(self):
        """пауза песни в плейлисте"""
        self.__playlist.pause()
        if self.__playing:
            self.__playing = False

    def add_song(self, name, duration):
        """добавление песни в плейлист"""
        self.__playlist.add_song(playlist_2.Song(name, duration))
        self.__post(name, duration)

    def play_prev(self):
        """воспроизведение следующей песни в плейлисте"""
        self.__playlist.play_prev()

    def play_next(self):
        """воспроизведение предыдущей песни в плейлисте"""
        self.__playlist.play_next()

    def delete_song(self):
        """удаление песни из плейлиста"""
        if not self.__playing:
            song = self.__playlist.delete_song()
            requests.delete('http://127.0.0.1:3000/playlist',
                            {'name': song.cur_song.name,
                             'playlist_name': self.__name,
                             'duration': song.cur_song.duration})

    def read_song(self):
        """чтение всех песен из плейлиста"""
        return requests.get('http://127.0.0.1:3000/playlist', {'playlist_name': self.__name})

    def __post(self, name, duration):
        """добавление песни в плейлист"""
        if not self.__playing:
            requests.post('http://127.0.0.1:3000/playlist', {'name': name,
                                                             'playlist_name': self.__name,
                                                             'duration': duration})

    def put(self, name, duration):
        """обновление записи"""
        if not self.__playing:
            requests.post('http://127.0.0.1:3000/playlist', {'name': name,
                                                             'playlist_name': self.__name,
                                                             'duration': duration})


# Пример использования
p = Playlist_api('Playlist_trance')
p.play()
