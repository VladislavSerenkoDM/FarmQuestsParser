import pandas as pd
from lxml import etree
import os
import shutil

# Define the input and output directories
input_dir = 'input'  # Directory containing the original XML files
output_dir = 'output'  # Directory to save the updated XML files

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the new quest amount and corresponding XML filenames from the Excel file
excel_file = 'quest_data.xlsx'  # Your Excel file name
df = pd.read_excel(excel_file)

# Assuming the Excel file has columns named 'CloseQuest', 'QuestXml', and 'Resource'
# 'CloseQuest' contains the new quest amount, 'QuestXml' contains the names of the XML files,
# and 'Resource' indicates whether the XML file should be processed
amount = df['Amount']
xml_files = df['QuestXml']
resources = df['Resource']
unique_collect = df['UniqueCollect']

# Iterate through each title and corresponding XML file
for amount, xml_filename, resource, unique_collect in zip(amount, xml_files, resources, unique_collect):
   
    resource = str(resource) if not pd.isna(resource) else ''
    unique_collect = str(unique_collect) if not pd.isna(unique_collect) else ''

    # Debugging prints to check values
    print(f"Processing file: {xml_filename}")
    print(f"Original Resource: {resource}, UniqueCollect: {unique_collect}")

    # Override resource with unique_collect if unique_collect is not empty
    if unique_collect:
        resource = unique_collect
   
   
   
    # Skip rows where 'Resource' is empty
    if pd.isna(resource):
        print(f"Skipping file '{xml_filename}' because 'Resource' is empty.")
        continue
    
    if pd.isna(unique_collect):
        resource = unique_collect    

    # Construct the full path to the XML file in the input directory
    xml_filename = str(xml_filename)
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
    resource = str(resource)
    amount = str(amount)
    print(resource)
    # Find the <ptr> element with the name attribute set to "onceTrigger" and update its value
    #    ___________________Data Context___________________

    for ptr in root.xpath(".//ptr[@name='GoalRequired']"):
        ptr.attrib['value'] = amount
        
    for ptr in root.xpath(".//ptr[@name='GoalRequired_Str']"):
        ptr.attrib['value'] = amount

    for ptr in root.xpath(".//ptr[@name='GoalName']"):
        ptr.attrib['value'] = resource        

    for ptr in root.xpath(".//ptr[@name='QuestLocationResources']"):
        ptr.attrib['value'] = resource   

    # Iterate over all elements in the XML tree to find onEndTrigger attribute
    #    ___________________Complete___________________
    
    for elem in root.iter():
        # Iterate over all attributes of the element
        for attr_name, attr_value in elem.attrib.items():
            # Check if the attribute value matches the old_value
            if attr_name == 'goalName':
                # Replace the attribute value with the new_value
                elem.set(attr_name, resource)

    for elem in root.iter():
    # Iterate over all attributes of the element
        for attr_name, attr_value in elem.attrib.items():
            # Check if the attribute value matches the old_value
            if attr_name == 'requiredValue':
                # Replace the attribute value with the new_value
                elem.set(attr_name, amount)


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

print("All quest amount have been updated.")

# Copy all XML files from output folder back to input folder
for xml_file in os.listdir(output_dir):
    if xml_file.endswith('.xml'):
        shutil.copyfile(os.path.join(output_dir, xml_file), os.path.join(input_dir, xml_file))