from pymongo import MongoClient as mc
import datetime
from certifi import where

username = "Abishek"
password = "Rajagiri123!"

ca = where()
uri = f"mongodb+srv://{username}:{password}@db.bpuc5.mongodb.net/test"

cl = mc(uri, tlsCAFile = ca)
db = cl['Attendance']

coll = [db['attendance'], db['students'], db['subjects']]

"""
ret = input("Enter RETID: ")
name = input("Enter name: ")
e1 = input("Enter subject code of departmental elective: ")
e2 = input("Enter subject code of global elective: ")

#retrieving results
x = c[1].find({
    "name": name
}, {
    "name": 1,
    "core": 1
})

for _ in x:
    for __ in _: print(f"{__}: {_[__]}")

#inserting records
d = {
    "RETID": ret,
    "name": name,
    "class": "S8 CSE a",
    "core": ['CS402', 'CS404', 'CS492'],
    "elective": [
        {
            "dept": e1
        },
        {
            "global": e2
        }
    ]
}

x = c[1].insert_one(d)
"""

date = datetime.datetime.now().strftime("%Y-%m-%d")
timetable = [
    ["08:30:00", "09:34:59"],
    ["09:35:00", "10:30:59"],
    ["10:45:00", "11:34:59"],
    ["12:35:00", "13:29:59"],
    ["13:30:00", "14:29:59"],
    ["14:40:00", "15:34:59"],
    ["15:35:00", "16:29:59"]
]


""" def initial():
    find = {}

    for _ in range(1, 8):
        up = {
            "$set": {
                f"{date}.P{_}": "0"
            }
        }

        x = coll[0].update_many(find, up)

    print(f"{x.modified_count} updated.")  """

def updateAttendance(l, t): #'l' contains id's of students in a set and 't' contains the time in string format

    for _ in range(len(timetable)):
        if timetable[_][0] <= t <= timetable[_][1]:
            P = f"P{_+1}"
            break

    #read list of students 'l'

    for _ in l:
        find = {
            "_id": _
        }

        up = {
            "$set": {
                f"{date}.{P}": "1"
            }
        }

        x = coll[0].update_many(find, up)

    #print(f"{x.modified_count} updated.")

    """
    from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://Abishek:Rajagiri123!@db.bpuc5.mongodb.net/test')
result = client['Attendance']['attendance'].aggregate([
    {
        '$project': {
            '2022-04-06': 1
        }
    }, {
        '$set': {
            '2022-04-06.P1': '0', 
            '2022-04-06.P2': '0', 
            '2022-04-06.P3': '0', 
            '2022-04-06.P4': '0', 
            '2022-04-06.P5': '0', 
            '2022-04-06.P6': '0', 
            '2022-04-06.P7': '0'
        }
    }
])
    """