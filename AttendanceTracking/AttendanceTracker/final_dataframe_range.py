from pymongo import MongoClient as mc
from certifi import where
from datetime import datetime, date, timedelta as td
from time import strftime
import pandas as pd

auth = []

"""with open("C:\\auth.txt") as d:
    auth = d.read().split('\0')"""

ca = where()
uri = f"mongodb+srv://Abishek:Rajagiri123!@db.bpuc5.mongodb.net/test"

db = mc(uri, tlsCAFile = ca)['Final']
null = {}
coll = [db['class'], db['att']]

def get_dataframe(start,end,cname):
    c = cname

    find, project = {
        "class": c
    }, {
        "_id": 0,
        "students.RETID": 1
    }

    x = coll[0].find(find, project)
    c = [_ for _ in x]
    ids = [_['RETID'] for _ in c[0]['students']]

    sd = [int(_) for _ in start.split('.')]
    sd = date(sd[0], sd[1], sd[2])

    ed = [int(_) for _ in end.split('.')]
    ed = date(ed[0], ed[1], ed[2])

    if sd > ed: sd, ed = ed, sd

    delta = td(days = 1)

    weekday = []

    while sd <= ed:
        if sd.strftime("%A") not in ["Sunday", "Saturday"]: 
            weekday.append(sd.strftime("%Y-%m-%d"))
        sd += delta

    dfl = {}

    for d in weekday:    
        data = []
        for _ in ids:
            find, project = {
                "RETID": _
            }, {
                "_id": 0,
                "RETID": 1,
                "P1": f"${d}.P1",
                "P2": f"${d}.P2",
                "P3": f"${d}.P3",
                "P4": f"${d}.P4",
                "P5": f"${d}.P5",
                "P6": f"${d}.P6",
                "P7": f"${d}.P7",
            }
            x = coll[1].find(find, project)
            dt = [_ for _ in x]
            data.append(dt)

        for _ in range(len(data)):
            data[_] = data[_][0]

        fd = pd.DataFrame(data)
        dfl[d] = fd
    return dfl