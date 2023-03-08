import threading
from time import sleep
import copy

class Song:
    """описание песни (длительность и название)"""
    def __init__(self, name, duration):
        self.duration = duration
        self.name = name


class Songs:
    """используется для реализации двусвязного списка с предыдущим, текущим и следующим обьектом песни"""
    def __init__(self, song):
        self.cur_song = song
        self.prev_song = self.next_song = None


class Playlist:
    def __init__(self):
        self.__playing = True
        self.__playing_song = False
        self.__lock = threading.Lock()
        self.__head = self.__tail = self.__cur_song = None

    def add_song(self, song):
        """Добавление песни в плейлист с использованием двусвязного списка"""
        with self.__lock:
            cur_song = Songs(song)

            if self.__head is None:
                self.__head = self.__tail = self.__cur_song = cur_song
            else:
                self.__tail.next_song = cur_song
                cur_song.prev_song = self.__tail
                self.__tail = cur_song

    def pause(self):
        """приостановка воспроизведения текущей песни"""
        print("Нажата кнопка паузы")
        if self.__playing:
            self.__playing = False

    def play(self):
        """обработка воспроизведения текущей песни"""
        print('Нажата кнопка плэй')
        if not self.__playing:
            self.__playing = True

    def play_song(self):
        """эмуляция воспроизведение текущей песни"""
        duration = self.__cur_song.cur_song.duration
        time_play = 0
        self.__start_song()
        self.play()

        while self.__playing_song:
            while self.__playing and time_play <= duration:
                print(f'Играет песня: {self.__cur_song.cur_song.name}\n время: {time_play} секунд')
                sleep(1)
                time_play += 1

            # если время воспроизведение закончилось запустим следующую песню, если есть
            if self.__playing:
                print(f'Закончилась песня {self.__cur_song.cur_song.name}')
                self.play_next()

    def play_next(self):
        """воспроизведение следующей песни в списке"""
        print("нажата кнопка следующая песня")
        if self.__cur_song.next_song is not None:
            self.__stop_song()
            self.__cur_song = self.__cur_song.next_song
            self.play_song()
        else:
            print('закончились песни в плейлисте')
            self.__stop_song()

    def play_prev(self):
        """воспроизведение предыдущей песни"""
        print("нажата кнопка песня")
        if self.__cur_song.prev_song is not None:
            self.__stop_song()
            self.__cur_song = self.__cur_song.prev_song
            self.play_song()

    def delete_song(self):
        """удаление текущей песни"""
        print("Удаление текущей песни из списка")
        if not self.__playing:
            current_song = copy.deepcopy(self.__cur_song)
            if self.__cur_song.prev_song is None:
                self.__head = self.__cur_song.next_song
            else:
                self.__cur_song.prev_song.song_next = self.__cur_song.next_song

            if self.__cur_song.next_song is None:
                self.__cur_song.__tail = self.__cur_song.prev_song
            else:
                self.__cur_song.next_song.prev_song = self.__cur_song.prev_song

            self.play_song()
            return current_song

    def __stop_song(self):
        """остановка воспроизведения песни"""
        self.__playing_song = False

    def __start_song(self):
        """продолжить воспроизведение песни"""
        self.__playing_song = True

