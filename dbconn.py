import sqlite3
def getconn():
    return sqlite3.connect('FaceBase.db')