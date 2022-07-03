import openpyxl

workbook = openpyxl.load_workbook("new_excel.xlsx")

sheet = workbook['new']
workbook.remove(sheet)
workbook.save("new_excel.xlsx")