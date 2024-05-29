import pandas as pd
from lxml import etree
import os
import shutil

# Define the input and output directories
input_dir = 'input'  # Directory containing the original XML files
output_dir = 'output'  # Directory to save the updated XML files

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the new quest titles and corresponding XML filenames from the Excel file
excel_file = 'quest_data.xlsx'  # Your Excel file name
df = pd.read_excel(excel_file)

# Assuming the Excel file has columns named 'new_title' and 'NameXml'
# 'ParentQuest' contains the new quest titles and 'NameXml' contains the names of the XML files
titles = df['Exp']
xml_files = df['NameXml']


# Iterate through each title and corresponding XML file
for new_title, xml_filename in zip(titles, xml_files):
    # Construct the full path to the XML file in the input directory
    xml_file_path = os.path.join(input_dir, xml_filename)
    
    # Check if the XML file exists in the input directory
    if not os.path.exists(xml_file_path):
        print(f"File {xml_file_path} does not exist.")
        continue

    # Load and parse the XML file
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(xml_file_path, parser)
    root = tree.getroot()

   
    '''
    ___________________Searching and replacing values block___________________

    '''

    new_title = str(new_title)

    # Iterate over all elements in the XML tree to find onEndTrigger attribute
    for elem in root.iter():
        # Iterate over all attributes of the element
        for attr_name, attr_value in elem.attrib.items():
            # Check if the attribute value matches the old_value
            if attr_name == 'experienceScores':
                # Replace the attribute value with the new_value
                elem.set(attr_name, new_title)


    '''
    ___________________Preserving the Look of the Source XML file___________________

    '''


    # Convert the XML tree to a string
    xml_str = etree.tostring(tree, pretty_print=True, xml_declaration=False, encoding='unicode')

    # Manually add a space before the self-closing tag '/>'
    xml_str = xml_str.replace('/>', ' />')

    # Construct the full path to the updated XML file in the output directory
    updated_xml_file_path = os.path.join(output_dir, xml_filename)
    
    # Write the updated XML to the new file in the output directory, preserving the desired format
    with open(updated_xml_file_path, 'w', encoding='utf-8') as file:
        # Write the XML declaration manually
        file.write('<?xml version="1.0"?>\n')
        # Write the rest of the XML content
        file.write(xml_str)

    print(f"The quest Exp has been updated to '{new_title}' in '{updated_xml_file_path}'.")

print("All quest Exp points have been updated.")

# Copy all XML files from output folder back to input folder
for xml_file in os.listdir(output_dir):
    if xml_file.endswith('.xml'):
        shutil.copyfile(os.path.join(output_dir, xml_file), os.path.join(input_dir, xml_file))