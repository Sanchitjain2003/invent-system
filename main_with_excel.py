import requests
import xlsxwriter

# main driver
main_flag = True
dash_count = 0
dash_index = []


# constants
workbook = xlsxwriter.Workbook('./python/vscode/invent-system/file.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0, "Manufacturer/Supplier")
worksheet.write(0,1, "SKU Code")
worksheet.write(0,2, "Location")
worksheet.write(0,3, "Barcode")
row_num = 1
col_num = 0
def create_barcode(data, dash_index,row_num, col_num):
    url = "https://barcode.tec-it.com/barcode.ashx?data={}".format(data)
    link = requests.get(url)
    if link.status_code != 200:
        print("Error accessing website, Terminating")
        workbook.close()
        exit()

    else:
        temp = col_num
        worksheet.write(row_num, temp, inp[:dash_index[0]])
        worksheet.write(row_num, temp+1, inp[dash_index[0]+1:dash_index[3]])
        worksheet.write(row_num, temp+2, inp[dash_index[3]+1:])
        worksheet.write(row_num, temp+3, url)
        row_num += 1
        col_num += 1
        return row_num, col_num

def string_format(data):
    for i in range(0,len(data)):
        if data[i] == '-':
            dash_index.append(i)
    return dash_index


while main_flag:
    inp = input()
    if inp.lower() == "exit":
        print("Program exiting")
        workbook.close()
        exit()
    
    else:
        dash_index = string_format(inp)
        row_num, col_num = create_barcode(inp, dash_index, row_num, col_num)
