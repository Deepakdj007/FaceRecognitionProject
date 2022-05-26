from pymongo import MongoClient as mc
from certifi import where
from datetime import date
from time import strftime
import pandas as pd
#import dataframe_image as dfi

auth = []

with open("C:\\auth.txt") as d:
    auth = d.read().split('\0')
    
ca = where()
uri = f"mongodb+srv://{auth[0]}:{auth[1]}@db.{auth[2]}.mongodb.net/test"
db = mc(uri, tlsCAFile = ca)['Final']

null = {}
coll = [db['class'], db['att']]

def view_today_att(class_date,class_name):
    d = class_date.split('-')
    d = [int(_) for _ in d]
    d = date(d[0], d[1], d[2]).strftime("%Y-%m-%d")

    find = {
        'class': class_name
    }
    
    project = {
        'students.RETID': 1,
        '_id': 0
    }
    
    l = list(coll[0].find(find, project))[0]
    l = [_['RETID'] for _ in l['students']]
    print(l)
    
    L = []
    for _ in l:
        #print(_, d)
        find, project = {
            'RETID': _
        }, {
            "_id": 0,
            "RETID": 1,
            d: 1
        }
        x = list(coll[1].find(find, project))[0]
        L.append(x)

    for _ in range(len(L)):
        L[_]['present'], L[_]['duty'], L[_]['absent'] = 0, 0, 0
        
   
    df = pd.json_normalize(L)
    """ 
    def HIGHLIGHT_COLOR(x):
        return ('background-color: ' + x.map({
            1: 'red',
            2: 'yellow',
            3: 'green'
        })).fillna('')"""
    """def HIGHLIGHT_COLOR(s):
        no = '0'
        return ['color: white','background-color: red' if v else 'color: black','background-color: white' for v no]"""
    df.columns = ['RETID', 'Present_hours', 'Duty_leaves', 'Absent_hours', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    df = df[['RETID'] + list(df.columns)[-7:] + list(df.columns)[1:4]]
    
    for i in range(len(df)):
        p, d, a = 0, 0, 0
        for hour in df.columns[1:8]:
            p, d, a = p+(df[hour][i] == 3), d+(df[hour][i] == 2), a+(df[hour][i] == 1)
        df['Present_hours'][i], df['Duty_leaves'][i], df['Absent_hours'][i] = p, d, a
    
    """    
    today = today.style.apply(HIGHLIGHT_COLOR).hide(axis='index')"""
    l = ["","A","D","P"]
    for i in range(len(df["RETID"])):
        for j in df.columns[1:8]:
            df[j][i] = l[df[j][i]]
    """dfi.export(today, "Todays Attendance.png")"""
    return df

    """writer = pd.ExcelWriter('Todays_Attendance.xlsx', engine='xlsxwriter')
    today.to_excel(writer, sheet_name='Todays Attendance')"""
def update_table(table, class_name,class_date):
    ret_id = table[0]
    attendance_marked = table[1:8]
    for i in range(len(attendance_marked)):
        if attendance_marked[i] == "":
            attendance_marked[i] = 0
        if attendance_marked[i] == "A":
            attendance_marked[i] = 1
        if attendance_marked[i] == "D":
            attendance_marked[i] = 2
        if attendance_marked[i] == "P":
            attendance_marked[i] = 3
    
    print(table[:-1])
    print(attendance_marked)
    for i in range(len(attendance_marked)):
        p = i+1
        find = {
            'RETID': ret_id
        }

        update = {
            '$set': {
                f'{class_date}.P{p}': attendance_marked[i]
            }
        }

        coll[1].update_one(find, update)