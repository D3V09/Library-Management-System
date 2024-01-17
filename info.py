import cv2 
from pyzbar.pyzbar import decode
from pydub import AudioSegment
import pandas as pd
from datetime import datetime
import csv

now_time = datetime.now()

data = []
cap = cv2.VideoCapture(0)


def search_and_write_to_csv(filename, search_term, data_to_write):
        matching_rows = []
        
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            
            for rows in csv_reader:
                if search_term in rows:
                    matching_rows.append(data_to_write)

        if matching_rows:
            with open(filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for matching_row in matching_rows:
                    matching_row.extend(data_to_write)
                    csv_writer.writerow(matching_row)
            print("Data written to the CSV file for matching rows.")
        else:
            print("No matching rows found.")

def check():
    
    while cap.isOpened():
        success,frame = cap.read() 
        frame  = cv2.flip(frame,1)
        detectedBarcode = decode(frame)
        if not detectedBarcode:
            print("No any Barcode Detected")
        
        else:
            for barcode in detectedBarcode:
                if barcode.data != "":
                    cv2.putText(frame,str(barcode.data),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                    # cv2.imwrite("bar.png",frame)
                    data.append(str(barcode.data))

        cv2.imshow('scanner' , frame)
        if cv2.waitKey(1) == ord('q'):
            break

check()

set_data = set(data)
csv_file_path = "data.csv"

with open(csv_file_path, mode="a", newline="") as csv_file:

    # full_data = csv_file.readlines()
    for row in set_data:

        # change byte string to normal string   
        clean_string = row[2:-1]
        byte_string = clean_string.encode('utf-8')
        r_id = byte_string.decode('utf-8')
        print(r_id)

        # searching 

        filename = csv_file_path 
        search_term = r_id
        data_to_write = now_time

        search_and_write_to_csv(filename, search_term, data_to_write)


print(f"Data has been written to {csv_file_path}")
