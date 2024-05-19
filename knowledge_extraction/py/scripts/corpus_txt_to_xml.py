import xml.etree.ElementTree as ET
from xml.dom import minidom


#change txt encoding (curly apostrophe) -- preprocessing!

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def text_to_xml(input_file, output_file):
    # Create the root element for the XML
    root = ET.Element("corpus")

    # Read the content of the text file with UTF-8 encoding and create a document element for each non-empty line
    with open(input_file, 'r', encoding='utf-8') as file:
        id=0
        for idx, line in enumerate(file, start=1):
            line = line.strip()
            if line:  # Skip empty lines
                document = ET.SubElement(root, "document")
                document.set("id", str(id))
                document.text = line
                id +=1

    # Prettify the XML
    prettified_xml = prettify(root)

    # Write the prettified XML to the output file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(prettified_xml)

if __name__ == "__main__":
    input_file_path = "C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\txt_for_classification\\result_whatabout.txt"
    output_file_path = "xml\whatabout_corpus.xml"
    text_to_xml(input_file_path, output_file_path)

