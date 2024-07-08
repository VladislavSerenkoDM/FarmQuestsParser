import os
import shutil
import pandas as pd

# Define paths
template_dir = 'templates'
output_dir = 'output'
input_dir = 'input'
excel_file = 'quest_data.xlsx'

# Read Excel file
df = pd.read_excel(excel_file)

# Ensure output and input directories exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(input_dir, exist_ok=True)

# Mapping quest types to template files
quest_type_to_template = {
    'Build': 'Build.xml',
    'Clear': 'Clear.xml',
    'Collect': 'Collect.xml',
    'StartCraft': 'StartCraft.xml',
    'Craft': 'Craft.xml',
}

# Process each row in the dataframe
for _, row in df.iterrows():
    quest_type = row['UniqueQuestType'] if pd.notna(row['UniqueQuestType']) else row['QuestType']
    quest_name = row['QuestID']
    
    # Get the corresponding template file
    template_file = quest_type_to_template.get(quest_type)
    
    if template_file:
        template_path = os.path.join(template_dir, template_file)
        output_path = os.path.join(output_dir, f"{quest_name}.xml")
        input_copy_path = os.path.join(input_dir, f"{quest_name}.xml")
        
        # Copy and rename the template file to the output directory
        shutil.copyfile(template_path, output_path)
        print(f"Copied {template_file} to {output_path}")

        # Copy the final XML file to the input directory
        shutil.copyfile(output_path, input_copy_path)
        print(f"Copied {output_path} to {input_copy_path}")
    else:
        print(f"No template found for quest type: {quest_type}")

print("Processing complete.")
