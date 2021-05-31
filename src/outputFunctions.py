import tableprint
import xlsxwriter

# Description : Output in console. Used tableprint to make the output in tabular format


def output_in_console(result):
    try:
        headers = ['ID', 'Title', 'Duration']
        width = [15, 80, 15]

        tableprint.table(result['videos'], headers, width=width)

        print("Total Duration : ", result['duration'])
    except Exception as e:
        print(e)

# Description : Output in text file


def output_in_txt_file(result):
    try:
        f = open("Output.txt", "w+")

        for video in result['videos']:
            f.write('ID : '+video[0]+'\n')
            f.write('Title : '+video[1]+'\n')
            f.write('Duration : '+video[2]+'\n')
            f.write('\n\n')

        f.write('Total Duration : '+result['duration'])

        f.close()
    except Exception as e:
        print(e)

# Description : Output in excel file


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
            {'header': 'Title'},
            {'header': 'Duration'},
        ]
        }

        worksheet.add_table('A4:C'+str(len(result['videos'])+4), options)

        workbook.close()
    except Exception as e:
        print(e)
