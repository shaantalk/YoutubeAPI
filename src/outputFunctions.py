import tableprint
import xlsxwriter

# ------------------------------------------------------------------------------------------------------------------
# Function Name : output_in_console
# Description : Output in console
# ------------------------------------------------------------------------------------------------------------------


def output_in_console(result):
    try:
        headers = ['ID', 'Link', 'Title', 'Duration']
        width = [15, 45, 80, 15]

        tableprint.table(result['videos'], headers, width=width)

        print("Total Duration : ", result['duration'])
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : output_in_txt_file
# Description : Output in text file
# ------------------------------------------------------------------------------------------------------------------


def output_in_txt_file(result):
    try:
        f = open("Output.txt", "w+")

        for video in result['videos']:
            f.write('ID : '+video[0]+'\n')
            f.write('Link : '+video[1]+'\n')
            f.write('Title : '+video[2]+'\n')
            f.write('Duration : '+video[3]+'\n')
            f.write('\n\n')

        f.write('Total Duration : '+result['duration'])

        f.close()
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Function Name : output_in_excel_file
# Description : Output in excel file
# ------------------------------------------------------------------------------------------------------------------


def output_in_excel_file(result):
    try:
        workbook = xlsxwriter.Workbook('Output.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write_row(0, 1, ['Total Duration', result['duration']])

        options = {'data': result['videos'],
                   'name': 'Videos',
                   'autofilter': False,
                   'columns': [
            {'header': 'ID'},
            {'header': 'Link'},
            {'header': 'Title'},
            {'header': 'Duration'},
        ]
        }

        worksheet.add_table('A4:D'+str(len(result['videos'])+4), options)

        workbook.close()
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------------------------------------------
