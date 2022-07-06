import openpyxl as xl

wb = xl.load_workbook("file.xlsx")

sheet = wb["Sheet1"]

cell = sheet["a1"]

cell = sheet.cell(1, 1)

# Create a for loop
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    print(cell.value)