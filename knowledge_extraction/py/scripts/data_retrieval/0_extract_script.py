

import os
import re

directory = 'C:\\Users\\lored\\OneDrive\\Desktop\\DigitalHumanities\\benaltrismo\\data\\Data\datasets-v5\\tasks-2-3\\train'
txt_files = []
label_files = []
text_data = []


# ...

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
            start_position=start_position-9
        end_position=end_position + 15 '''
        
        text_file.seek(start_position)
        text = text_file.read(end_position - start_position)
        return text

'''
def extract_article_number(file_path):
    # Extract the sequence of numbers from the file path
    match = re.search(r'article(\d+).task3.labels', file_path)
    if match:
        return match.group(1)
    else:
        return None '''
def extract_article_number(file_path):
    # Extract the sequence of numbers from the file path
    match = re.search(r'article(\d+)', file_path)
    if match:
        return match.group(1)
    else:
        return None

def main():
    
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            f = str(f).replace('\\', '/')
            if f.endswith('.txt'):
                txt_files.append(str(f))
            elif f.endswith('.task3.labels'):
                label_files.append(str(f))


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
                    text_file_path=text.replace('.task3.labels', '.txt')
                    article=extract_article_number(text)
                    extracted_text = read_text_file(text_file_path, start_position, end_position)

                    # Print the extracted text and article number
                    print(f"Article {article} - Technique: {list[1]} - Extracted Text:", extracted_text  ) 
                    text_data.append(extracted_text)
                
                elif  len(list) >= 2 and  "Red_Herring" in list[1] :
                    start_position, end_position = map(int, list[2:])
                    text_file_path=text.replace('.task3.labels', '.txt')
                    article=extract_article_number(text)
                    extracted_text = read_text_file(text_file_path, start_position, end_position)

                    # Print the extracted text and article number
                    print(f"Article {article} - Technique: {list[1]} - Extracted Text:", extracted_text  ) 
                    text_data.append(extracted_text)



if __name__ == "__main__":
    main()

# You can iterate through label_files separately if needed
'''
print(len(text_data))
with open("C:/Users/lored/OneDrive/Desktop/DigitalHumanities/benaltrismo/data/Data/datasets-v5/tasks-2-3/train/0_extracted_sem_eval_2021.txt", "w") as output:
        for t in text_data:
            output.write(str(t)+ "\n\n")

'''