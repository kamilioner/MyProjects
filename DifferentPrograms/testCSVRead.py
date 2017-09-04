import csv

my_csv_file = open('C:/Users/Kamil/Desktop/test.csv', "r")
my_csv_reader = csv.reader(my_csv_file, delimiter=',')
my_csv_data = list(my_csv_reader)

print(my_csv_data)