
import pandas as pd

# Load the Excel file
excel_file = pd.ExcelFile(r'C:\Users\Prathamesh\Desktop\Book1.xlsx')

# Specify the sheet name and the column containing the data
sheet_name = 'Sheet1'
column_name = 'Date'

# Read the data from the specified range
data = pd.read_excel(excel_file, sheet_name=sheet_name, usecols=[column_name])

# Convert the date column to string format
data[column_name] = data[column_name].astype(str)

# Search for a particular range (e.g., date range)
start_date = '25/03/2023'
filtered_data = data[data[column_name].str.contains(start_date)]

# Save filtered data to a text file
with open('output.txt', 'w') as output_file:
    for row in filtered_data.iterrows():
        output_file.write(str(row[1][column_name]) + '\n')

print("Filtered data for the date", start_date, "has been saved to output.txt")
