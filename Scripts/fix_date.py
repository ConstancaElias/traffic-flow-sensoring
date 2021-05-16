import csv
import sys
from datetime import datetime
import pandas as pd

def fix_date(date):
    '''
    add one hour to the input date. For example, date "05/08/2020 16:55" will become "05/08/2020 17:55"

    date - in format - "DD/MM/YYYY HH:MM

    returns new date with fixed hour
    '''
    seconds = ' '
    
    date_day, time = date.split('_')
    if len(time.split(':')) == 2:
        hour, minutes = time.split(':')
    else:
        hour, minutes, seconds = time.split(':')

    hour_int = int(hour)

    if hour_int == 23:
        new_hour = 00
    else:
        new_hour = hour_int + 1

    #year, month, day = date_day.split('-')

    #new_date = day +'/' + month + '/' + year + ' ' + str(new_hour) + ':' + minutes
    new_date = date_day + ' ' + str(new_hour) + ':' + minutes

    
    #new_datetime = datetime.strptime(new_date, '%y-%m-%d %H:%M:%S')

    #return pd.to_datetime(new_date) 
    return new_date

def main():

    if len(sys.argv) == 1:
        print("Input filename and output filename are missing")
        return ''
    
    elif len(sys.argv) == 2:
        print("Output filename is missing")
        return ''

    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]

        dic = {}

        #read input file and fix date for each row
        with open(input_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')


            line_count = 0
            idx_timestamp = 0
            for row in csv_reader:
                if line_count != 0:
                    row[idx_timestamp] = fix_date(row[idx_timestamp])
                    dic[line_count] = row
                
                else:
                    dic[line_count] = row
                    for i in range(len(row)):
                        if row[i] == "timestamp":
                            idx_timestamp = i
                            break

                line_count += 1

            #write new dictionary to output file
            with open(output_filename, 'w', newline = '') as outfile:
                outputfile = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                
                for i in range(len(dic)):
                    outputfile.writerow(dic[i])


if __name__ == "__main__":
    main()