from openpyxl import workbook, load_workbook
wk = load_workbook("Data Entry.xlsx")
ws = wk.active
ws.title = "Sales Data"
ws.append(['Date', 'Sales Rep', 'Product', 'Units', 'Price'])
ws.append(['date', 'person', 'product', 'units', 'price'])

wk.save('Data Entry.xlsx')