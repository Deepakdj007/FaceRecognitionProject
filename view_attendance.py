from pymongo import MongoClient as mc
from certifi import where
from pandas import DataFrame as df

username = "Abishek"
password = "Rajagiri123!"

ca = where()
uri = f"mongodb+srv://{username}:{password}@db.bpuc5.mongodb.net/test"

cl = mc(uri, tlsCAFile = ca)
db = cl["Attendance"]

c = sorted(db.list_collection_names())
coll = [db[_] for _ in c]

"""fque = {
    "_id": "RET18CS005"
}

x = coll[0].find(fque)"""

date = input("Enter date: ")

x = coll[0].find({
    f"{date}": {
        "$exists": True
    }
})

for _ in x:
    print(_)
    """for __ in _: 
        print(_[__])"""
"""l = []
for _ in x[0]: l.append(x[0][_])

print(l)"""