import os
import pandas as pd
import numpy as np


# Function to calculate tree height based on DBH
def calculate_height(dbh):
    if dbh > 0:  # Ensure DBH is positive to avoid math domain error
        return 1.37 + 10 * np.log(dbh)
    else:
        return None


# Folder containing the .csv files
folder_path = "sp"  # Change this if the folder is named differently

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Folder '{folder_path}' not found. Please check the path.")
else:
    # List all .csv files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    if not csv_files:
        print("No CSV files found in the specified folder.")
    else:
        for csv_file in csv_files:
            # Read the CSV file
            file_path = os.path.join(folder_path, csv_file)
            try:
                data = pd.read_csv(file_path)
                print(f"Processing file: {csv_file}")

                # Check if 'DBH' column exists
                if 'DBH' not in data.columns:
                    print(f"File '{csv_file}' does not contain a 'DBH' column. Skipping...")
                    continue

                # Calculate tree height and add it as a new column
                data['Height_m'] = data['DBH'].apply(lambda dbh: calculate_height(dbh))

                # Save the updated dataset (overwriting the original file)
                data.to_csv(file_path, index=False)
                print(f"File updated and saved: {file_path}")

            except Exception as e:
                print(f"Error processing file '{csv_file}': {e}")
