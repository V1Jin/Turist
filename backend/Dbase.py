import sqlite3

path = "D:/Programming/Turism/backend/"

    

baseDir = 'D:/Programming/Turism/backend/audio/'



def connect():
    conn = sqlite3.connect("orgs.db")

    return conn

def close(conn):
    conn.close()

def getOrgs():
    conn = connect()
    cursor = conn.cursor()

    text = '''
SELECT * FROM организации
'''
    cursor.execute(text)
    data = []

    for i in cursor.fetchall():
        smallData = {
            "name": i[1],
            "coordinates": [i[2],i[3]],
            "info": i[4],
            "img": i[5]
            }
        data.append(smallData)
    close(conn)
    return data

def addOrg(data):
    conn = connect()
    cursor = conn.cursor()

    text = '''
INSERT INTO организации (название, широта, долгота, описание, img) VALUES (?,?,?,?,?)
'''
    if ("img" not in data.keys()): cursor.execute(text, (data["name"], data["coordinates"][0], data["coordinates"][1], data["info"], None ))
    else: cursor.execute(text, (data["name"], data["coordinates"][0], data["coordinates"][1], data["info"], data["img"] ))
    conn.commit()
    close(conn)



'''CREATE TABLE "организации" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"название"	TEXT,
	"широта"	REAL,
	"долгота"	REAL,
	"описание"	TEXT,
  "img" TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);'''