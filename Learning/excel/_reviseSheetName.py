import openpyxl

workbook = openpyxl.load_workbook("new_excel.xlsx")

sheet = workbook['Mysheet1'] #選擇使用特定的sheet
sheet.title = 'Fruit' #更改特定的sheet的名稱為'Fruit'
workbook.save("new_excel.xlsx")