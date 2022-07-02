import openpyxl

workbook = openpyxl.load_workbook("new_excel.xlsx")

sheet = workbook['Fruit']
target = workbook.copy_worksheet(sheet)
target.title = 'new'
workbook.save("new_excel.xlsx")