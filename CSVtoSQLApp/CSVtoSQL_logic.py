import pymysql
import re
import csv


def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def insertCSVtoSQL(localost_name, port_name, user_name, password_name, db_name, table_name, file_name, file_delimiter):
    data_types_list = []
    line_chosen = 1  # 0 is 'there is no first line with names', 1 is 'there is a first line with names'

    create_table_string = 'CREATE TABLE '
    create_table_string += table_name
    create_table_string += ' ('

    conn = pymysql.connect(host=localost_name, port=port_name, user=user_name, passwd=password_name, db=db_name)
    cur = conn.cursor()


    my_csv_file = open(file_name, "r")
    my_csv_reader = csv.reader(my_csv_file, delimiter=file_delimiter)
    my_csv_data = list(my_csv_reader)


    # for line in range(len(my_csv_data)):
    if line_chosen == 0:
        for word in range(len(my_csv_data[line_chosen])):
            data_types_list.append('expr_' + word + 1)

    if line_chosen == 1:
        line = 1
        for word in range(len(my_csv_data[line])):
            if my_csv_data[line][word] == '':
                data_types_list.append('VARCHAR(200)')
            else:
                if isint(my_csv_data[line][word].rstrip()):
                    data_types_list.append('BIGINT')
                else:
                    if isfloat(my_csv_data[line][word].rstrip()):
                        data_types_list.append('FLOAT')
                    else:
                        data_types_list.append('VARCHAR(200)')

    for cl in range(int(len(data_types_list))):
        create_table_string += ((my_csv_data[0][cl]).rstrip() + ' ' + (data_types_list[cl].rstrip() + ', '))

    create_table_string = create_table_string[:-1]
    create_table_string = create_table_string[:-1]
    create_table_string += ')'
    # print(create_table_string)
    # print('')
    cur.execute(create_table_string)

    for line in range(len(my_csv_data)):
        if line != 0:
            insert_row_string = 'INSERT INTO '
            insert_row_string += db_name
            insert_row_string += '.'
            insert_row_string += table_name
            insert_row_string += ' VALUES ('
            for word in range(len(my_csv_data[line])):
                my_csv_data[line][word] = re.sub("'", "''", my_csv_data[line][word])
                if isfloat(my_csv_data[line][word].rstrip()):
                    insert_row_string += (my_csv_data[line][word].rstrip() + ", ")
                else:
                    if data_types_list[word] != 'VARCHAR(200)':
                        insert_row_string += ("0, ")
                    else:
                        insert_row_string += ("'" + my_csv_data[line][word].rstrip() + "'" + ", ")
            insert_row_string = insert_row_string[:-1]
            insert_row_string = insert_row_string[:-1]
            insert_row_string += ')'

            #print(insert_row_string)
            cur.execute(insert_row_string)

    my_csv_file.close()

    conn.commit()

    cur.close()
    conn.close()
