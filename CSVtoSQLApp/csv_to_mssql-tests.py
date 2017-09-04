from sqlalchemy import create_engine
from urllib import parse
from pandas import read_csv
from getopt import getopt, GetoptError
from sys import exit, exc_info, argv
from time import time
from pathlib import Path
from logging import error, ERROR, basicConfig


def main(arguments):

    input_file = ''
    output_table = ''

    try:
        opts, args = getopt(arguments, "hi:o:t:", ["ifile=", "use"],)
    except GetoptError:
        print('csv_to_mssql.py -i <"input file path"> -o <"output table name">')
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('csv_to_mssql.py -i <"input file path"> -o <"output table name">')
            exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in "-o":
            output_table = arg

    if (input_file != '') and (output_table != ''):
        try:
            change_table(input_file, output_table)
        except IOError:
            print("Inappropriate file path.")
    else:
        print("Input file path and output table name are required.")
        print("Write csv_to_mssql -h for help")


def error_logger(message):
    error(message)
    error(str(exc_info()))


def change_table(file_name, table):
    basicConfig(filename='csv_to_mssql.log', level=ERROR,
                format='%(asctime)s  %(message)s', filemode='a', datefmt='%d-%m-%Y %I:%M:%S')
    server = 'MC0ZMAWC'
    database = 'test'

    # con_str = "DRIVER={SQL Server Native Client 11.0};SERVER=,port;DATABASE=vcmdb;UID=user;PWD=pwd"
    con_str = "DRIVER={SQL Server Native Client 11.0};SERVER=" + server + ";DATABASE=" + database + ";trusted_connection=yes"
    params = parse.quote(con_str)
    print('Connecting to ' + server + ' server and ' + database + ' database:')
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    try:
        conn = engine.connect().connection
        cursor = conn.cursor()
    except:
        print('Connection failed')
        error_logger('Connection to server/database failed due to:')
        return -1

    print('Connection succeeded.')
    print('')

    print('Reading a file:')
    lengths = []

    try:
        df = read_csv(file_name, encoding="ISO-8859-1", low_memory=False)
    except:
        print('An error has occurred while loading the file.')
        error_logger('Reading a file failed due to:')
        return -1

    for col in list(df.columns):
        df[col] = df[col].astype(str)
        lengths.append(df[col].map(len).max() + 1)

    print('File loaded.')
    print('')

    print('Dropping a table:')
    drop_table_string = "IF OBJECT_ID('" + table + "', 'U') IS NOT NULL DROP TABLE " + table + ";"

    try:
        cursor.execute(drop_table_string)
        conn.commit()
    except:
        print('An error has occurred while dropping a table.')
        error_logger('Dropping a table failed due to:')
        return -1

    print('Table ' + table + ' has been dropped.')
    print('')

    print('Creating a table:')
    create_table_string = 'CREATE TABLE ' + table + ' ('

    for a, b in zip(list(df.columns), lengths):
        create_table_string += '[' + a + '] varchar(' + str(b) + '), '

    create_table_string = create_table_string[:-2]
    create_table_string += ');'

    try:
        cursor.execute(create_table_string)
        conn.commit()

    except:
        print('An error has occurred while creating a table.')
        error_logger('Creating a table failed due to:')
        return -1

    print('Table ' + table + ' has been created.')
    print('')

    print('Trying to bulk insert data to the table:')
    bulk_insert = " BULK INSERT " + table + " FROM '" + str(Path(file_name).resolve()) + \
                  "' WITH (FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');"
    ts = time()

    try:
        cursor.execute(bulk_insert)
        conn.commit()
    except:
        print('An error has occurred while inserting to table.')
        error_logger('Dropping a table failed due to:')
        return -1

    print("All " + str(df.shape[0]) + " rows have been inserted in " + str(time() - ts) + " seconds")
    print("with an average speed of " + str(df.shape[0] / (time() - ts)) + " records per second.")
    error('File "' + file_name + '" has been successfully inserted to ' + table + '.')

if __name__ == "__main__":
    main(argv[1:])

change_table('checkval.csv', 't1')
# python csv_to_mssql.py -i .\checkval.csv -o "t1"
