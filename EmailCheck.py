
import os
import re

import pandas as pd
import xlrd
data = open("data.txt" , "r")
data = data.readlines()
d = dict()
for lines in data:
    lines = lines.strip()
    l = lines.split('-')
    print(l)
    d[l[0]] = d.get(l[0],0)+int(l[1])

print("data -------------------> ",d)


for root, dirs, files in os.walk("Downloads"):
    for directory in dirs:
        for r, d, f in os.walk("Downloads/" + directory):
            excel_file = ""
            text_file = ""
            try:
                for fl in f:
                    if fl.endswith("xlsx"):
                        excel_file = fl
                        print("Excel File ---------", excel_file)
                    if fl.endswith("txt"):
                        text_file = fl
                if excel_file != '':
                    print("------------- " + directory + "-------------")

                    df = pd.read_excel("Downloads/" + directory + "/" + excel_file)
                    wb = xlrd.open_workbook("Downloads/" + directory + "/" + excel_file)
                    sheet = wb.sheet_by_index(0)
                    email = sheet.cell_value(0, 9)
                    # print(email)
                    l = list(df[email])
                    u = list(df['URL'])

                    try:
                        for i in l:
                            if '@' not in i:
                                print("Email e jamela ase - > ", i, " index number -> ", l.index(i), ' , URL----->',
                                      u[l.index(i)])
                    except:
                        print("exception value ", i, " index number ->", l.index(i))
            except Exception as e:
                print(e)
                df = pd.read_excel(excel_file)
                wb = xlrd.open_workbook(excel_file)
                sheet = wb.sheet_by_index(0)
                email = sheet.cell_value(0, 9)
                # print(email)
                l = list(df[email])
                u = list(df['URL'])

                try:
                    for i in l:
                        if '@' not in i:
                            print("Email e jamela ase - > ", i, " index number ->", l.index(i), 'URL----->',
                                  u[l.index(i)])
                except:
                    print("exception value ", i, " index number ->", l.index(i))






