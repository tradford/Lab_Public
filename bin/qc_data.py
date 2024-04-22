import pandas as pd
import os
from datetime import datetime

# Replace 'your_file_path.txt' with the actual path to your text file
directory_path = 'path'

# The threshold date and time
threshold_datetime = datetime.strptime("20240313_000000", "%Y%m%d_%H%M%S")

# List to hold DataFrames
dfs = []

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    # Check if the file name matches the pattern (basic check)
    if filename.startswith("MgCl2Brine") and filename.endswith(".txt"):
        # Extract the date_time part from the file name and convert it to datetime
        date_time_str = filename.split("_")[1] + "_" + filename.split("_")[2].split(".")[0]
        file_datetime = datetime.strptime(date_time_str, "%Y%m%d_%H%M%S")
        
        # Check if the file's date_time is greater than the threshold
        if file_datetime > threshold_datetime:
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)
            # Load the file into a DataFrame and append to the list
            df = pd.read_csv(file_path, sep='\t')
            dfs.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Now, final_df is a DataFrame containing all the combined data. You can use final_df.head() to display the first few rows.
print(final_df.head())

# Define the path for the Excel file you want to create
excel_file_path = r'path'

# Save the DataFrame to an Excel file
final_df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f'Data saved to {excel_file_path}')