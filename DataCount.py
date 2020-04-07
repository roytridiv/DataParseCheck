
import os

import xlrd



for root, dirs, files in os.walk("Downloads"):
    for directory in dirs:
        #print(directory)
        for r, d, f in os.walk("Downloads/" + directory):
            excel_file = ""
            text_file = ""
            for fl in f:
                #print(f.index(fl) == 0)
                if fl.endswith("xlsx"):
                    excel_file = fl
                if fl.endswith("txt"):
                    text_file = fl
            if excel_file != '' and text_file != '':
                text_file = open("Downloads/" + directory+"/"+text_file, "r")
                text_file = text_file.readlines()
                total_lines = 0

                for i in text_file:
                    if i.startswith("Total"):
                        l = i.split()
                        total_lines = int(l[len(l) - 1])
                print("Report ----> ", total_lines)

                wb = xlrd.open_workbook("Downloads/" + directory+"/"+excel_file)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0, 0)
                print("Excel Sheet ---->", sheet.nrows - 1)
                if sheet.nrows - 1 == total_lines:
                    print("Data Counts matched for * " + directory + " *")
                else:
                    print("Data Counts did not matched for * " + directory + " * ")






