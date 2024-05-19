import os
import re

#directory = 'C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\semEval2023\\data\\en\\train-labels-subtask-3-spans'
#articles_dir='C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\semEval2023\\data\\en\\train-articles-subtask-3'
directory_dev = 'C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\semEval2023\\data\\en\\dev-labels-subtask-3-spans'
articles_dev='C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\semEval2023\\data\\en\\dev-articles-subtask-3'
txt_files = []
label_files = []
text_data = []

def read_labels_file(labels_file_path):
    with open(labels_file_path, 'r') as labels_file:
        # Read all lines from the file
        lines = labels_file.readlines()

        # Remove leading and trailing whitespaces from each line
        cleaned_lines = [line.strip() for line in lines]

        # Return the list of cleaned lines
        return cleaned_lines
    
def read_text_file(text_file_path, start_position, end_position):
    with open(text_file_path, 'r', encoding='utf-8') as text_file:
        '''
        if start_position>9:
            start_position=start_position-8
        end_position=end_position + 35
        '''
        
                  
        text_file.seek(start_position)
        text = text_file.read(end_position - start_position)
        return text
    
def extract_article_number(file_path):
    # Extract the sequence of numbers from the file path
    match = re.search(r'article(\d+)', file_path)
    if match:
        return match.group(1)
    else:
        return None

def main():
    for filename in os.listdir(directory_dev):
        f = os.path.join(directory_dev, filename)
        if os.path.isfile(f):
            f = str(f).replace('\\', '/')
            if f.endswith('.txt'):
                label_files.append(str(f))
    for filename in os.listdir(articles_dev):
        f = os.path.join(articles_dev, filename)
        if os.path.isfile(f):
            f = str(f).replace('\\', '/')
            if f.endswith('.txt'):
                txt_files.append(str(f))

    for text in label_files:
    # Read the line from the labels file
            labels_line = read_labels_file(text)
            columns=[]
            # Extract information from the labels line
            for line in labels_line: 
                l=line.split('\t')
                columns.append(l)
            #print (extract_article_number(text), columns)
            
            for list in columns:
                    
                        if len(list) >= 2 and  "Whataboutism" in list[1] :
                            
                            start_position, end_position = map(int, list[2:])
                            text_file_path=text.replace('-spans', '')
                            text_file_path=text_file_path.replace('labels', 'articles')
                            text_file_path=text_file_path.replace('-articles-subtask-3.txt', '.txt')
                            article=extract_article_number(text)
                            extracted_text = read_text_file(text_file_path, start_position, end_position)

                            # Print the extracted text and article number
                            print(f"Article {article} - Technique: {list[1]} - Extracted Text:", extracted_text ) 
                            text_data.append(extracted_text)
                        '''
                        elif  len(list) >= 2 and  "Red_Herring" in list[1] :
                            start_position, end_position = map(int, list[2:])
                            text_file_path=text.replace('-spans', '')
                            text_file_path=text_file_path.replace('labels', 'articles')
                            text_file_path=text_file_path.replace('-articles-subtask-3.txt', '.txt')
                            article=extract_article_number(text)
                            extracted_text = read_text_file(text_file_path, start_position, end_position)

                            # Print the extracted text and article number
                            print(f"Article {article} - Technique: {list[1]} - Extracted Text:", extracted_text  ) 
                            text_data.append(extracted_text)
                        
'''

if __name__ == "__main__":
    main()
print(len(text_data))
'''
#print(len(text_data)) -> 65
with open("C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\semEval2023\\data\\0_extracted_text_23.txt", "w", encoding='utf-8') as output:
        for t in text_data:
            output.write(str(t)+ "\n\n")
            '''

#C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\txt\\...
with open("C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\semEval2023\\data\\0_extracted_dev_text_23.txt", "w", encoding='utf-8') as output:
        for t in text_data:
            output.write(str(t)+ "\n\n")