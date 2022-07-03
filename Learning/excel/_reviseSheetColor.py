import openpyxl

workbook = openpyxl.load_workbook("new_excel.xlsx")

# sheet = workbook.active #選擇正在使用的sheet
sheet = workbook['Mysheet1'] #選擇使用特定的sheet
sheet.sheet_properties.tabColor = "1072BA" #sheet的顔色改成藍色
workbook.save("new_excel.xlsx")