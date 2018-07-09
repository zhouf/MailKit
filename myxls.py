import xlrd
wb = xlrd.open_workbook('R:\\prj2\\2018届本科毕业论文正常答辩名单.xlsx')

wb.sheet_names()

sh = wb.sheet_by_index(0)
sh = wb.sheet_by_name(u'Sheet1')

print("rows=" + str(sh.nrows) + " cols=" + str(sh.ncols))

for rownum in range(sh.nrows):
    print(sh.row_values(rownum))

first_column = sh.col_values(0)
print(first_column)

cell_A1 = sh.cell(0,0).value
cell_C4 = sh.cell(rowx=3,colx=2).value

print(cell_A1)
print(cell_C4)