import csv
import sys


def fix_date(date):
    '''
    add one hour to the input date. For example, date "05/08/2020 16:55" will become "05/08/2020 17:55"

    date - in format - "DD/MM/YYYY HH:MM

    returns new date with fixed hour
    '''
    
    day, time = date.split(' ')
    hour, minutes = time.split(':')

    hour_int = int(hour)

    if hour_int == 23:
        new_hour = 00
    else:
        new_hour = hour_int + 1


    new_date = day + ' ' + str(new_hour) + ':' + minutes

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
        print(input_filename)
        print(output_filename)

        dic = {}

        #read input file and fix date for each row
        with open(input_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    row[7] = fix_date(row[7])
                    dic[line_count] = row
                
                else:
                    dic[line_count] = row

                line_count += 1

            #write new dictionary to output file
            with open(output_filename, 'w', newline = '') as outfile:
                outputfile = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                
                for i in range(len(dic)):
                    print(dic[i])
                    outputfile.writerow(dic[i])


if __name__ == "__main__":
    main()