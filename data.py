import csv
from datetime import datetime

now_time = datetime.now()

def write_into_csv(filename , data_to_write):
    with open(filename, mode='a', newline='') as file:

        csv_writer = csv.writer(file)
        csv_writer.writerow(data_to_write)

    file.close()

def search_and_write_to_csv(filename, search_term, data_to_write):

    with open(filename, mode='r', newline='') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if search_term in row:
                print(row)
                write_into_csv(filename , data_to_write)

    file.close()


search_and_write_to_csv("data.csv", '11757', now_time)