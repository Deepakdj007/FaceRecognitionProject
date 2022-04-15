#import pymongo
from imp import init_builtin
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


def initializeDay(d):
    find = {}

    for _ in range(1, 8):
        up = {
            "$set": {
                f"{d}.P{_}": "0"
            }
        }

        x = coll[0].update_many(find, up)
        
def initializePeriod(P):
    find = {}
    up = {
        "$set": {
            f"{date}.{P}": "0"
        }
    }
    x = coll[0].update_many(find, up)

def updateAttendance(l, t): #'l' contains id's of students in a set and 't' contains the time in string format
    """ if t < timetable[0][0] or timetable[0][0] < t <= timetable[0][1]:
        initial(date)

    elif t > timetable[-1][-1] or timetable[-1][0] < t < timetable[-1][1]:
        day = datetime.datetime.now().strftime("%w")
        if day == 5:
            date1 = datetime.datetime.now() + datetime.timedelta(3)
            date1 = datetime.datetime.now().strftime("%Y-%m-%d")

    """
   
    find = {
        f"{date}": {
            "$exists": False
        }
    }

    x = coll[0].count_documents(find)

    if x:
        initializeDay(date)
   
    for _ in range(len(timetable)):
        if timetable[_][0] <= t <= timetable[_][1]:
            P = f"P{_+1}"
            break

    #setting attendance of a period to 0
    initializePeriod(P)
    
    #marking attendance
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


