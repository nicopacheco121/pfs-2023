import openpyxl
import openpyxl.utils.cell
#abrimos el excel. El data_only=True sirve para no ver las formulas sino los valores
workbook = openpyxl.load_workbook('CierreROFEX.xlsx',data_only=True)

print(workbook.sheetnames)
sheet = workbook.worksheets[0]

title =[cell.value for cell in sheet[1]]
print(title)
column = sheet[openpyxl.utils.cell.get_column_letter(title.index("Ajuste")+1)]

#sheet.
dict = {"posicion":sheet[openpyxl.utils.cell.get_column_letter(title.index("Posicion")+1)]
        ,"ajuste":sheet[openpyxl.utils.cell.get_column_letter(title.index("Ajuste")+1)]}

for pos,ajuste in zip(dict["posicion"],dict["ajuste"]):
    if pos == "Posicion":
        continue
    print(pos.value,ajuste.value)

newSheet = workbook.create_sheet("MiPrueba")
newSheet["A1"] = "matias"
workbook.save('CierreROFEX.xlsx')
workbook.remove(newSheet)
workbook.save('CierreROFEX.xlsx')


workbook = openpyxl.load_workbook('dataset_reporte_covid_sitio_gobierno.xlsx',data_only=True)
sheet = workbook.worksheets[0]

title =[cell.value for cell in sheet[1]]
out = dict.fromkeys(["min_date","min","max_date","max"])
for row in sheet:
    if row[2].value == "ocupacion_de_camas_sistema_publico":
        if not(out["min"]) or out["min"]>=row[4].value:
            out["min_date"] = row[0].value
            out["min"] = row[4].value
        if not(out["max"]) or out["max"]<=row[4].value:
            out["max_date"] = row[0].value
            out["max"] = row[4].value

print(out)

