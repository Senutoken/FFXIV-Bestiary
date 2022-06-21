# Reading an excel file using Python
import xlrd # pip3 install xlrd
import pathlib # For path finding

# Give the location of the file
pathlib.Path("")
path = '../Bestiary.csv'

# Open Workbook
wb = xlrd.open_workbook(path)
ws = wb.sheet_by_index(0)

# Functions #

def ReadExcel():
    for row in range(ws.nrows):
        for col in range(ws.ncols):
            if col == 1 or col == 5 or col == 6:
                print("{: <10}".format(ws.cell_value(row, col)), end=' ')
            else:
                print("{: <30}".format(ws.cell_value(row, col)), end=' ')
        print()  # New line

def sortName():
    print("Sorting by name")

ReadExcel()

