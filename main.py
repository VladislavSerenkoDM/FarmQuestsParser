import pandas as pd
import os
import update_quest

# Define file paths
excel_file = 'quest_titles.xlsx'
xml_folder = 'input'
output_folder = 'output'

# Read the Excel file
df = pd.read_excel(excel_file)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through each row in the Excel file
for index, row in df.iterrows():
    xml_filename = row['filename']
    new_title = row['new_title']
    
    # Construct the full path to the XML file
    xml_file = os.path.join(xml_folder, xml_filename)
    
    # Construct the output file path
    output_file = os.path.join(output_folder, xml_filename)
    
    # Check if the XML file exists
    if os.path.exists(xml_file):
        # Call the function to update the quest title
        update_quest.update_quest_title(excel_file, xml_file, output_file)
        print(f"Updated {xml_file} with new title '{new_title}'")
    else:
        print(f"File {xml_file} not found, skipping.")

print("All files have been processed.")
