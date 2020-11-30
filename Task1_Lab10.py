import csv

# .txt Files accessible when using PYCHARM, but not on VISUAL STUDIO CODE
def format_txt_to_csv(txtfile):
    csv_format_data = []
    with open(txtfile, 'r') as txt_file:
        data_list = txt_file.readlines()
        for datum in data_list:
            datum_with_comma = datum.replace(' ', ',')
            datum_list = datum_with_comma.split(',')
            if len(datum_list) < 2:
                datum_list.insert(0, ' ')
            datum_list[1] = datum_list[1].rstrip('\n')
            csv_format_data.append(datum_list)
    return csv_format_data

def create_csv(csvfile):
    with open(csvfile, 'w', newline="") as csv_file:
        headers = ['First Name', 'Count']
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(headers)
        if csvfile == 'boysnames.csv':
            csv_writer.writerows(format_txt_to_csv('2000-BoysNames_Collateral.txt'))
            csv_created = 'boysnames.csv'
            return csv_created
        elif csvfile == 'girlsnames.csv':
            csv_writer.writerows(format_txt_to_csv('2000-GirlsNames_Collateral.txt'))
            csv_created = 'girlsnames.csv'
            return csv_created

user_create_file = input('Enter the gender for which you want to create the csv file [M/F]: ')
if user_create_file.capitalize() == 'M':
    csv_created = create_csv('boysnames.csv')
    print('FILE NAME--> ' + csv_created)
elif user_create_file.capitalize() == 'F':
    csv_created = create_csv('girlsnames.csv')
    print('FILE NAME--> ' + csv_created)
