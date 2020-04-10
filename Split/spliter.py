from datetime import datetime
import xlsxwriter

file = open("ItalyModT1italyReport.txt", "r")
file = file.readlines()

workbook = xlsxwriter.Workbook('test3.xlsx')
worksheet = workbook.add_worksheet()


row = 1
column = 0
data = ""


for line1 in file:
    line1 = line1.split("~~")
    for line2 in line1:
        line2 = line2.split("##")
        if '~' in line2[1]:
            i = line2[1]
            i = i[:-2]
            print(row, int(line2[0]), i)
            worksheet.write(row, int(line2[0]), i)
        else:
            print(row, line2[0], line2[1])
            worksheet.write(row, int(line2[0]), line2[1])



    row += 1


workbook.close()