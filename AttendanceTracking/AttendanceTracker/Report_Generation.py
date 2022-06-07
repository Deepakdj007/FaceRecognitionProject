from . import final_dataframe_range as fdr
import os
import shutil
import numpy as np
import pandas as pd
import calendar
from datetime import datetime
from fpdf import FPDF
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

def get_report(from_date,to_date,c):
    dff = fdr.get_dataframe(from_date.replace('-','.'),to_date.replace('-','.'),c)

    df = dff[from_date.replace('.','-')]
    #df

    present, duty, absent = [], [], []
    for _ in df.columns[1:]:
        p, d, a = 0, 0, 0
        for __ in range(len(df["RETID"])):
            p += (df[_][__] == 3)
            d += (df[_][__] == 2)
            a += (df[_][__] == 1)
        present.append(p)
        duty.append(d)
        absent.append(a)

    for i in range(0, len(present)):
        present[i] = int(present[i])
        duty[i] = int(duty[i])
        absent[i] = int(absent[i])

    # create DataFrame
    graph = {"Present": present, "Duty Attendance": duty, "Absent": absent}

    df2 = pd.DataFrame(graph, index=["P1", "P2", "P3", "P4", "P5", "P6", "P7"])
    #df2

    import matplotlib.pyplot as plt

    def plot(data: pd.DataFrame, filename: str) -> None:
        plt.figure(figsize=(12, 4))

        #sns.set(style='white')
        df2.plot(kind='bar', stacked=True, color=['green', 'skyblue', 'red'])

        # labels for x & y axis
        plt.xlabel('Hours')
        plt.ylabel('No. of students')

        # title of plot
        plt.title("Today's attendance")


        plt.grid(color='#F2F2F2', alpha=1, zorder=0)
        plt.xticks(fontsize=9)
        plt.yticks(fontsize=9)
        plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close()
        return

    plot(data=df2, filename='today1.png')
    """ 
   from IPython.display import Image
    Image("today1.png")
    """

    class PDF(FPDF):
        def __init__(self):
            super().__init__()
            self.WIDTH = 210
            self.HEIGHT = 297

        def header(self):
            # Custom logo and positioning
            # Create an `assets` folder and put any wide and short image inside
            self.image('F:\Deepak_Jose_RSET\FaceRecognitionProject\AttendanceTracking\AttendanceTracker\_reports.png', 0, 0, 22)
            self.set_font('Arial', 'B', 11)
            self.cell(self.WIDTH - 80)
            self.cell(60, 1, 'Daily Report', 0, 0, 'R')
            self.ln(20)

        def footer(self):
            # Page numbers in the footer
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128)
            self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

        def page_body(self, images):
            # Determine how many plots there are per page and set positions
            # and margins accordingly
            if len(images) == 3:
                self.image(images[0], 15, 25, self.WIDTH - 30)
                self.image(images[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
                self.image(images[2], 15, self.WIDTH / 2 + 90, self.WIDTH - 30)
            elif len(images) == 2:
                self.image(images[0], 15, 25, self.WIDTH - 30)
                self.image(images[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
            else:
                self.image(images[0], 15, 25, self.WIDTH - 30)

        def print_page(self, images):
            # Generates the report
            self.add_page()
            self.page_body(images)

    pdf = PDF()

    pdf.print_page(["today1.png"])

    pdf.output('Report.pdf', 'F')


"""get_report('2022.05.17','2022.05.17','S8CSEa')"""





