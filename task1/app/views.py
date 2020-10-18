from django.shortcuts import render
from django.conf import settings
import csv
from django.http import HttpResponse
from pprint import pprint

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста

    # infl_data = []
    with open(settings.INFLATION_DATA_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        raw_infl_data = [row for row in reader]

        table_top_row = raw_infl_data[0]
        table_top_row = table_top_row[0].split(';')

        infl_table_data = []
        totals_row = []


        for row in raw_infl_data:
            for record in row:
                str_line = record.split(';')

                line = []
                for obj in str_line:

                    if obj == '':
                        line.append('-')

                    try:
                        line.append(int(obj))
                    except:
                        try:
                            line.append(float(obj))
                        except:
                            pass
                if len(line) > 0:
                    year = line[0]
                    total_value = line[-1]
                    line.pop(0)
                    line.pop(-1)
                    infl_data = (year, line, total_value)
                    infl_table_data.append(infl_data)
                    totals_row.append(total_value)





    context = {
        'infl_table_data': infl_table_data,
        'table_top_row': table_top_row,
    }


    return render(request, template_name,
                  context)