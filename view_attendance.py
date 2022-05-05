from pymongo import MongoClient as mc
from certifi import where
import pandas as pd
import dataframe_image as dfi

ca = where()
cl = mc("mongodb+srv://Abishek:Rajagiri123!@db.bpuc5.mongodb.net/test",tlsCAFile = ca)
db = [cl[_] for _ in sorted(cl.list_database_names())]
coll = [db[1][_] for _ in sorted(db[0].list_collection_names())]

data = list(coll[0].find())
df = pd.DataFrame(data)
df = pd.json_normalize(data)

date = input("Enter date: ")


def HIGHLIGHT_COLOR(x):
    return ('background-color: ' + x.map({
        "0": 'red'
    })).fillna('')



"""def HIGHLIGHT_COLOR(s):
    no = '0'
    return ['color: white','background-color: red' if v else 'color: black','background-color: white' for v no]"""


l = ["_id"]
col = [colmn for colmn in df.columns if f'{date}' in colmn]
l.extend(col)
today = df[l]
today.columns = ['RETID','P1','P2','P3','P4','P5','P6','P7']
today = today.style.apply(HIGHLIGHT_COLOR).hide(axis='index')

    
dfi.export(today,"Todays Attendance.png")

"""writer = pd.ExcelWriter('Todays_Attendance.xlsx', engine='xlsxwriter')
today.to_excel(writer, sheet_name='Todays Attendance')"""






