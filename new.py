import cv2
from pyzbar.pyzbar import decode
import csv
from datetime import datetime

def search_and_write_to_csv(file_name, search_value, updated_data):
    with open(file_name, 'r', newline='') as file:
        rows = list(csv.reader(file))

    # Find and update the specific row
    updated = False
    for row in rows:
        if search_value in row:
            row[:] += updated_data  # Replace the entire row
            updated = True
            break  # Stop searching once the first match is found

    # If the row was updated, write the changes back to the same file
    if updated:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    else:
        print("Value not found in the CSV file, no changes made.")

def check():
    data = set()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)
        detected_barcodes = decode(frame)

        if not detected_barcodes:
            print("No Barcode Detected")
        else:
            for barcode in detected_barcodes:
                if barcode.data != "":
                    cv2.putText(frame, str(barcode.data), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                    data.add(str(barcode.data))

        cv2.imshow('scanner', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return data

if __name__ == "__main__":
    now_time = datetime.now()
    csv_file_path = "data.csv"
    data = check()

    for row in data:
        clean_string = row[2:-1]
        r_id = clean_string.encode('utf-8').decode('utf-8')

        # Searching and writing to CSV
        filename = csv_file_path
        search_term = r_id
        data_to_write = [now_time]
        search_and_write_to_csv(filename, search_term, data_to_write)

    print(f"Data has been written to {csv_file_path}")