from pandas import read_csv
from getopt import getopt, GetoptError
from sys import exit, exc_info, argv
from pathlib import Path
from logging import error, ERROR, basicConfig
from os.path import splitext, basename


def main(arguments):
    input_file = ''
    output_table = 'new_table'
    output_dir = '.'
    database = 'vCMDB'

    try:
        opts, args = getopt(arguments, "hi:o:t:d:")
    except GetoptError:
        print('csv_to_mssql.py -i <input file path> -o <"output directory" - default: current directory> -t <"table name" - default: "new_table"> -d <"database name" - default: "vCMDB">')
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('csv_to_mssql.py -i <input file path> -o <"output directory" - default: current directory> -t <"table name" - default: "new_table"> -d <"database name" - default: "vCMDB">')
            exit()
        elif opt in "-i":
            input_file = arg
        elif opt in "-o":
            output_dir = arg
        elif opt in "-t":
            output_table = arg
        elif opt in "-d":
            database = arg

    if input_file != '':
        try:
            create_sql_file(input_file, output_table, output_dir, database)
        except IOError:
            print("Inappropriate file path.")
    else:
        print("Input file path is required.")
        print('Write "python csv_to_mssql -h" for help')


def error_logger(message):
    error(message)
    error(str(exc_info()))


def create_sql_file(file_name, table, output_dir, database):
    basicConfig(filename='csv_to_mssql.log', level=ERROR,
                format='%(asctime)s  %(message)s', filemode='a', datefmt='%d-%m-%Y %I:%M:%S')

    print('')
    print('Reading a file:')
    lengths = []

    try:
        df = read_csv(file_name, encoding="ISO-8859-1", low_memory=False)
    except:
        print('An error has occurred while loading the file.')
        error_logger('ERROR: Reading a file failed due to:')
        return -1

    for col in list(df.columns):
        df[col] = df[col].astype(str)
        lengths.append(df[col].map(len).max() + 1)

    print('File loaded.')

    print('Creating a sql file:')

    use_db_string = "use " + database

    drop_table_string = "IF OBJECT_ID('" + table + "', 'U') IS NOT NULL DROP TABLE " + table + ";"

    create_table_string = 'CREATE TABLE ' + table + ' ('
    for a, b in zip(list(df.columns), lengths):
        create_table_string += '[' + a + '] varchar(' + str(b) + '), '
    create_table_string = create_table_string[:-2]
    create_table_string += ');'

    bulk_insert_string = "BULK INSERT " + table + " FROM '" + str(Path(file_name).resolve()) + \
                         "' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\\n');"

    output_file_name = 'insert_' + splitext(basename(file_name))[0] + '.sql'

    try:
        with open(output_dir + '/' + output_file_name, 'w') as f:
            f.write(use_db_string + '\n' + drop_table_string + '\n' + create_table_string + '\n' + bulk_insert_string + '\n' + 'go')
    except:
        print('An error has occurred while creating the output file.')
        error_logger('ERROR: Creating a file failed due to:')
        return -1

    print("Done")
    error('File "' + output_file_name + '" has been successfully created.')


if __name__ == "__main__":
    main(argv[1:])

create_sql_file('./checkval.csv', 't1', '.', 'test')
# python csv_to_mssql.py -i .\checkval.csv -o "t1"
# python csv_to_mssql.py -i "checkval.csv" -t "test_table" -d "test_db" -o "."
