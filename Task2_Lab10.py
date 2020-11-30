import csv

# *Task 2:
def read_csv(csvname):
    with open(csvname, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
    return data_list
print('Files--> boysnames.csv / girlsnames.csv')
user_view_file = input('Enter the File Name for the csv file you want to view: ')
data_list = read_csv(user_view_file)
for datum in data_list:
    print(datum)
