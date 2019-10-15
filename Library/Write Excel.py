import openpyxl
# Create Workbook first (this is temporary workbook, we have to save it at the end of the excel setup)

wk = openpyxl.Workbook()

sheet1 = wk.active
sheet1.title = "Test1"

sheet1['A1'].value  = 'Testing this code1'
sheet1['A2'].value  = 'Testing this code2'
sheet1['A3'].value  = 'Testing this code3'


#Creating new sheet under the workbook

wk.create_sheet('Test2')
sh2 = wk["Test2"]

sh2['A1'].value = 'Testing again 1'
sh2['A2'].value = 'Testing again 1'
sh2['A3'].value = 'Testing again 1'

#Saving the workbook

wk.save("C:\Users\mopawar\PycharmProjects\Creating_NewFramework\Myexcel_write.xlsx")

