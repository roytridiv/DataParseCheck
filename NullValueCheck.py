
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
                count = 0
                file_ger = ("Downloads/" + directory+"/"+excel_file)
                wb = xlrd.open_workbook(file_ger)
                sheet = wb.sheet_by_index(0)
                print(sheet.ncols, sheet.nrows)
                for row in range(sheet.nrows):
                    for column in range(sheet.ncols):
                        if (sheet.cell_value(row, column) == "" or
                                sheet.cell_value(row, column) == " " or
                                sheet.cell_value(row, column) == None):
                            print("Row number -> ", row + 1, "COLUMN number -> ", column + 1)
                            # countReport.write(
                            #     "Row number -> " + str(row + 1) + "COLUMN number -> " + str(column + 1) + "\n")
                            count = count + 1




