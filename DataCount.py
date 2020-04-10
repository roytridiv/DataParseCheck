
import os

import xlrd


data = open("data.txt" , "r")
data = data.readlines()
da = dict()
for lines in data:
    lines = lines.strip()
    l = lines.split('-')
    #print(l)
    da[l[0]] = da.get(l[0],0)+int(l[1])

#print("data -------------------> ",da)
try:
    for root, dirs, files in os.walk("Downloads"):
        for directory in dirs:
            # print(directory)
            for r, d, f in os.walk("Downloads/" + directory):
                excel_file = ""
                text_file = ""
                for fl in f:
                    # print(f.index(fl) == 0)
                    if fl.endswith("xlsx"):
                        excel_file = fl
                    if fl.endswith("txt"):
                        text_file = fl
                if excel_file != '' and text_file != '':
                    print("------------- <<<<<<<< " + directory + " >>>>>>> -------------")
                    text_file = open("Downloads/" + directory + "/" + text_file, "r")
                    text_file = text_file.readlines()
                    total_lines = 0

                    for i in text_file:
                        if i.startswith("Total"):
                            l = i.split()
                            total_lines = int(l[len(l) - 1])
                    print("Report ----> ", total_lines)

                    wb = xlrd.open_workbook("Downloads/" + directory + "/" + excel_file)
                    sheet = wb.sheet_by_index(0)
                    sheet.cell_value(0, 0)
                    print("Excel Sheet ---->", sheet.nrows - 1)
                    if da.get(directory) > sheet.nrows - 1:
                        print("-------------Difference of values for ***"+directory+"*** --------------", (da.get(directory) - sheet.nrows - 1) )
                    else:
                        print("---------- MATCHED According to URL count for ***" + directory + "*** ----------")
                    if sheet.nrows - 1 == total_lines:
                        print("Data Counts matched for * " + directory + " *")
                    else:
                        print("Data Counts did not matched for * " + directory + " * ")

except Exception as e:
    print(e)


