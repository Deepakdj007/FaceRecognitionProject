from pymongo import MongoClient as mc
from certifi import where
from datetime import date
from time import strftime

auth = []

with open("C:\\auth.txt") as d:
    auth = d.read().split('\0')

ca = where()
uri = f"mongodb+srv://{auth[0]}:{auth[1]}@db.{auth[2]}.mongodb.net/test"

db = mc(uri, tlsCAFile = ca)['Final']

null = {}
coll = [db['class'], db['att']]
"""
x = coll[1].delete_many(null)
x = coll[1].insert_one(
    {
        "RETID": "RET17CS013"
    }
)
"""
#---------------------------
"""
l0 = [205, 190, 60]
l1 = ["CS", "EC", "IT"]

for _ in range(len(l0)):
    for __ in range(1, l0[_]):
        x = coll[1].insert_one(
            {
                "RETID": f'RET18{l1[_]}{"0" if __ in range(100) else ""}{"0" if __ in range(10) else ""}{__}'
            }
        )
"""
#---------------------------
"""
from datetime import date, timedelta
from time import strftime

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2022, 3, 7)
end_date = date.today()
for single_date in daterange(start_date, end_date):
    if single_date.strftime("%w") != "0":
        update = {
            "$set": {
                single_date.strftime("%Y-%m-%d"): {
                    "P1": 0,
                    "P2": 0,
                    "P3": 0,
                    "P4": 0,
                    "P5": 0,
                    "P6": 0,
                    "P7": 0
                }
            }
        }

        x = coll[1].update_many(null, update)
"""
#---------------------------
"""
if date.today().strftime("%w") != "0":
    update = {
        "$set": {
            date.today().strftime("%Y-%m-%d"): {
                "P1": 0,
                "P2": 0,
                "P3": 0,
                "P4": 0,
                "P5": 0,
                "P6": 0,
                "P7": 0
            }
        }
    }

    x = coll[1].update_many(null, update)
"""
#---------------------------
def validate(C, P):
    find = {
        'class': C
    }

    x = coll[0].count_documents(find)
    
    if not x:
        print("ERROR: invalid class")
        quit()

    if P not in range(1, 8):
        print("ERROR: invalid hour number")
        quit()

def updateAttendance(C, P, l):
    find = {
        'class': C
    }

    project = {
        'students.RETID': 1
    }

    x = coll[0].find(find, project)
    
    id = []
    for _ in x: 
        for __ in _['students']:
            id.append(__['RETID'])

    for _ in l:
        find = {
            'RETID': _
        }

        update = {
            '$set': {
                f'{date.today().strftime("%Y-%m-%d")}.P{P}': 3
            }
        }

        x = coll[1].update_one(find, update)

    for _ in id:
        if _ not in l:
            find = {
                'RETID': _
            }

            update = {
                '$set': {
                    f'{date.today().strftime("%Y-%m-%d")}.P{P}':1
                }
            }

            x = coll[1].update_one(find, update)

"""    
    find = {
        date.today().strftime('%Y-%m-%d'): {
            '$exists': False
        }
    }

    x = coll[1].count_documents(find)

    if x:
        update = {
            '$set': {
                date.today().strftime('%Y-%m-%d'): {
                    'P1': 0,
                    'P2': 0,
                    'P3': 0,
                    'P4': 0,
                    'P5': 0,
                    'P6': 0,
                    'P7': 0
                }
            }
        }

        x = coll[1].update_many(null, update)
               
    for _ in l:
        find = {
            'RETID': _
        }

        update = {
            '$set': {
                f'{date.today().strftime("%Y-%m-%d")}.P{P}': 1
            }
        }

        x = coll[0].update_many(find, update)

    for _ in 
"""
print("poetry")