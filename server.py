from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sqlite3


app = Flask(__name__)
api = Api()


class Process(Resource):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('playlist.db')
        self.cursor = self.db.cursor()

    def get(self):
        """выборка всех песен плейлиста"""
        pars = request.args
        self.cursor.execute(f"""SELECT *
                                FROM Playlist
                                WHERE playlist_name = '{pars['playlist_name']}'""")
        return self.cursor.fetchall()

    def delete(self):
        """удаление песни из плейлиста"""
        pars = request.args
        self.cursor.execute(f"""DELETE FROM Playlist
                                WHERE name = '{pars['name']}'
                                  AND playlist_name = '{pars['playlist_name']}' 
                                  AND duration = '{pars['duration']}'""")
        self.db.commit()

    def post(self):
        """добавление записи в плейлист"""
        pars = request.args
        self.cursor.execute(f"""INSERT INTO Playlist VALUES('{pars['name']}', 
                                                            '{pars['playlist_name']}',
                                                            '{pars['duration']})""")
        self.db.commit()

    def put(self):
        """обновление записи в плейлисте"""
        pars = request.args
        self.cursor.execute(f"""UPDATE Playlist SET duration = '{pars['duration']}' 
                                WHERE playlist_name = '{pars['playlist_name']}'
                                  AND name = '{pars['name']}'""")
        self.db.commit()


api.add_resource(Process, '/playlist')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
