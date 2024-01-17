import csv

# Specify the file name
file_name = 'your_file.csv'
search_value = 'value_to_search'  # The value you want to search for
updated_data = ['new_data1', 'new_data2', 'new_data3']  # The updated data for the same row

# Open the CSV file in read mode
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
