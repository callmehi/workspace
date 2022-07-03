import openpyxl

workbook = openpyxl.load_workbook("new_excel.xlsx")

sheet = workbook['Sheet']
sheet.sheet_state = 'hidden' #選擇使用特定的sheet並'隱藏'

# sheet = workbook['BBB']
# sheet.sheet_state = 'visible'  #選擇使用特定的sheet並'顯示'

workbook.save("new_excel.xlsx")