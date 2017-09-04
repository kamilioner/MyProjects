import csv

table_name = 'test_table2'
data_list = []
file_delimiter = '|'
new_file_delimiter = ','
data_quotechar = '*'
new_data_quotechar = "\""

my_csv_file = open("new_test.csv", "r")
my_new_csv_file = open("procesy.csv", "w")
my_csv_reader = csv.reader(my_csv_file, delimiter=file_delimiter, quotechar=data_quotechar)
my_csv_data = list(my_csv_reader)

for line in range(len(my_csv_data)):
    for word in range(len(my_csv_data[line])):
        my_new_csv_file.write(new_data_quotechar + my_csv_data[line][word] + new_data_quotechar + new_file_delimiter)
    my_new_csv_file.write('\n')

my_new_csv_file.close()
my_csv_file.close() 