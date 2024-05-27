import pandas as pd
from lxml import etree

def update_quest_title(excel_file, xml_file, output_file):
    # Read the new quest title from an Excel file
    df = pd.read_excel(excel_file)

    # Assuming the Excel file has a column named 'new_title' with the new quest titles
    new_title = df['new_title'].iloc[0]  # Get the first title from the Excel file

    # Load and parse the XML file
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(xml_file, parser)
    root = tree.getroot()

    # Find the <ptr> element with the name attribute set to "title" and update its value
    for ptr in root.xpath(".//ptr[@name='title']"):
        ptr.attrib['value'] = new_title

    # Convert the XML tree to a string
    xml_str = etree.tostring(tree, pretty_print=True, xml_declaration=False, encoding='unicode')

    # Manually add a space before the self-closing tag '/>'
    xml_str = xml_str.replace('/>', ' />')

    # Write the updated XML to a new file, preserving the desired format
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write the XML declaration manually
        file.write('<?xml version="1.0"?>\n')
        # Write the rest of the XML content
        file.write(xml_str)

    print(f"The quest title has been updated to '{new_title}' in '{output_file}'.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python update_quest.py <excel_file> <xml_file> <output_file>")
    else:
        update_quest_title(sys.argv[1], sys.argv[2], sys.argv[3])
