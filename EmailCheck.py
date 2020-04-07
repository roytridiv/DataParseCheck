
import os

import pandas as pd
import xlrd


for root, dirs, files in os.walk("Downloads"):
    for directory in dirs:
        for r, d, f in os.walk("Downloads/" + directory):
            excel_file = ""
            text_file = ""
            for fl in f:
                if fl.endswith("xlsx"):
                    excel_file = fl
                if fl.endswith("txt"):
                    text_file = fl
            if excel_file != '':
                print("------------- "+directory+ "-------------")

                df = pd.read_excel("Downloads/" + directory+"/"+excel_file)
                wb = xlrd.open_workbook(excel_file)
                sheet = wb.sheet_by_index(0)
                email = sheet.cell_value(0, 9)
                #print(email)
                l = list(df[email])
                u = list(df['URL'])

                try:
                    for i in l:
                        if '@' not in i:
                            print("Email e jamela ase - > ", i, " index number ->", l.index(i), 'URL----->',
                                  u[l.index(i)])
                except:
                    print("exception value ", i, " index number ->", l.index(i))





