from pymongo import MongoClient as mc
from certifi import where
from datetime import date
from time import strftime
import pandas as pd

"""auth = []
with open("C:\\auth.txt") as d:
    auth = d.read().split('\0')"""

ca = where()
uri = f"mongodb+srv://Abishek:Rajagiri123!@db.bpuc5.mongodb.net/test"
db = mc(uri, tlsCAFile = ca)['Final']
null = {}
coll = [db['class'], db['att']]
lowatt = []

def low_attendance(Class_name):
    C = Class_name
    x = coll[0].aggregate(
        [
            {
                '$match': {
                    'class': C
                }
            }, {
                '$project': {
                    '_id': 0,
                    'class': 0, 
                    'students.attendancescore.attended': 0, 
                    'students.attendancescore.total': 0, 
                    'timetable': 0
                }
            }
        ]
    )

    a = [_ for _ in x][0]['students']
    df = []

    for _ in a:
        df.append([_['RETID'], _['details']['name'], _['details']['contact_details']['phone'][0], _['details']['contact_details']['email'][0], _['details']['DOB'], _['attendancescore'][0]['score'], _['attendancescore'][1]['score'], _['attendancescore'][2]['score'], _['attendancescore'][3]['score'], _['attendancescore'][4]['score']])
    df = pd.DataFrame(df, columns = ["RETID", "Name", "Phone_no", "Email_ID", "DOB", "Subject_1", "Subject_2", "Subject_3", "Subject_4", "Subject_5"])
    #print(df[["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]])
    dff = df[["Name", "Email_ID"] + list(df.columns[-5:])]

    for _ in range(len(dff)):
        subs = []
        for sub in list(dff.columns[-5:]):
            if dff[sub][_] < 75:
                subs.append((sub, dff[sub][_]))
        lowatt.append((dff['Name'][_], [dff['Email_ID'][_], subs]))
    """print(lowatt)"""
    names = [_[0] for _ in lowatt]
    email = [_[1][0] for _ in lowatt]

    df2=pd.DataFrame()

    for i in range(1,6):
        #df1 = pd.DataFrame(df.loc[df['Subject_'+str(i)] < 75])
        df1 = df[df['Subject_'+str(i)]<75]
        df2 = df2.append(df1, ignore_index=True)
    df2 = df2.drop_duplicates()
    
    return names,email,df2

def message_content(email):
    for pos in range(len(lowatt)):
        if lowatt[pos][1][0] == email: break
    message = f"""Dear {lowatt[pos][0]},
You have low attendance in the following subjects:
    """
    for sub in lowatt[pos][1][1]:
        message += f"""
{sub[0]}:\t{sub[1]}%"""
    message += """
    
Please take care."""
    return message 

def main():
    low_attendance()
    #message_content()
if __name__ == "__main__":
    main()