from pymongo import MongoClient as mc
from certifi import where
from datetime import date
from time import strftime
import pandas as pd
import dataframe_image as dfi

"""pd.options.display_max_rows = None
pd.options.display_max_cols = None"""
auth = []

with open("C:\\auth.txt") as d:
    auth = d.read().split('\0')

ca = where()
uri = f"mongodb+srv://{auth[0]}:{auth[1]}@db.{auth[2]}.mongodb.net/test"

db = mc(uri, tlsCAFile = ca)['Final']
null = {}
coll = [db['class'], db['att']]

def HIGHLIGHT_COLOR(x):
    return ('background-color: ' + x.map({
        1: 'red',
        2: 'yellow',
        3: 'green'
    })).fillna('')

def view_att(class_date,class_name):    
    d = class_date
    print(d)
    d = d.split('-')
    d = [int(_) for _ in d]

    d = date(d[0], d[1], d[2]).strftime("%Y-%m-%d")
    print(d)
    project = {
        "RETID": 1,
        d: 1,
        "_id": 0
    }
    C = class_name
    find = {
    'class': C
    }

    project = {
    'students.RETID': 1,
    '_id': 0
    }

    l = list(coll[0].find(find, project))

    if not l:
        print("ERROR: invalid class")
        quit()

    l = [_['RETID'] for _ in l[0]['students']]

    L = []
    for _ in l:
        find = {
            'RETID': _
        }

        project = {
            "_id": 0,
            "RETID": 1,
            d: 1
        }
        L.extend([_ for _ in list(coll[1].find(find, project))])
    df = pd.json_normalize(L)

    l = ["RETID"]
    col = [colmn for colmn in df.columns if d in colmn]
    l.extend(col)
    today = df[l]
    today.columns = ['RETID', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    today = today.style.apply(HIGHLIGHT_COLOR).hide(axis='index')
    
    """dfi.export(today, "Todays Attendance.png")"""
    return today
"""writer = pd.ExcelWriter('Todays_Attendance.xlsx', engine='xlsxwriter')
today.to_excel(writer, sheet_name='Todays Attendance')"""
"""view_att()"""