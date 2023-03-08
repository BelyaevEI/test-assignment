import playlist
import time
import threading

#создание плэйлиста
p = playlist.Playlist()

#создание песен
list_songs = [playlist.Song(5, 'Beethoven-symphony 5'),
              playlist.Song(6, 'Aria-freedom'),
              playlist.Song(3, 'Rammstein-Deutschland')]

for song in list_songs:
    p.add_song(song)

#Проверка работоспособности плейлиста
p.play()


#Проверка работа функции паузы
thread_1 = threading.Thread(target=p.play_song)
thread_1.start()
time.sleep(3)
p.pause()
time.sleep(3)
p.play()


#Проверка функций следующая и предыдущая песни
thread_2 = threading.Thread(target=p.play_song)
thread_2.start()
time.sleep(3)
p.pause()
time.sleep(3)
p.play_next()

