'''import pandas as pd
import os
import re

articles_dev='C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\SemEval_23_en\\en\\dev-labels-subtask-3'
txt_files = []
label_files = []

dataset=[]

def read_labels_file(labels_file_path):
    with open(labels_file_path, 'r', encoding='utf-8') as labels_file:
        # Read all lines from the file
        lines = labels_file.readlines()

        # Remove leading and trailing whitespaces from each line
        cleaned_lines = [line.strip() for line in lines]

        # Return the list of cleaned lines
        return cleaned_lines
def read_text_file(text_file_path, start_position, end_position):
    with open(text_file_path, 'rb', encoding='utf-8') as text_file:
        text_file.seek(start_position)
        try:
            text = text_file.read((end_position) - (start_position)).decode('utf-8', errors='replace')
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError in file {text_file_path}: {e}")
            text = "not_decoded"  # Handle the error by assigning an empty string or any other suitable value
        return text


def main():
    
    
    labels_df=pd.DataFrame(columns=['ID', 'Line', 'Labels'])
    for filename in os.listdir(articles_dev):
        f = os.path.join(articles_dev, filename)
        if os.path.isfile(f):
            f = str(f).replace('\\', '/')
        
            if f.endswith('.txt'):
                label_files.append(str(f))
    for filename in os.listdir(articles_dev):
        f = os.path.join(articles_dev, filename)
        if os.path.isfile(f):
            f = str(f).replace('\\', '/')
            if f.endswith('.template'):
                txt_files.append(str(f))
    print (len(label_files))


    for text in label_files:
    # Read the line from the labels file
            labels_line = read_labels_file(text)
            for line in labels_line: 
                l=line.split('\t')
                if len(l)>=3:
                    
                    #if  "Whataboutism" not in l[2] :
                        #if 'Red_Herring' not in l[2]:
                # Assuming your file is tab-separated
                            file_path = text
                            df = pd.read_csv(file_path, sep='\t', header=None, names=['ID', 'Line', 'Labels'], on_bad_lines='skip')

                        # Display the DataFrame
                        
                            labels_df=pd.concat([labels_df, df])

            # Filter rows where Labels column is not empty
            #non_empty_labels = df[df['Labels'].notna()]

            # Display rows with non-empty labels
            
    ids=list(labels_df['ID'])
    id=[]
    lines=[]
    texts=[]
    
    for text in txt_files:
    # Read the line from the labels file
            t_line = read_labels_file(text)
            for line in t_line: 
                l=line.split('\t')
                id.append(int(l[0]))
                lines.append(l[1])
                texts.append(l[2])              
                
                        
    lines=  pd.Series(lines)
    id= pd.Series(id)
    texts=pd.Series(texts)    
    data={'ID':id,
          'Line':lines,
          'Text':texts}  
    d=pd.concat(data, axis=1)  

    all=pd.merge(labels_df, d, on='ID')           #dataset.append(l[2])
    #print(all['Labels'])
    # Filter rows where 'Whataboutism' is not present in the 'Labels' column
    non_whataboutism_rows = all[~all['Labels'].str.contains('Whataboutism', na=False)]

    # Separate dataframe with only 'Whataboutism' rows
    whataboutism_rows = all[all['Labels'].str.contains('Whataboutism', na=False)]

    

    #print("Non-Whataboutism Rows:")
    #print(non_whataboutism_rows['Text'].drop_duplicates().head(40))

    #print("\nWhataboutism Rows:")
    #print(whataboutism_rows['Labels'])

    with open("C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\datasets\\0_my_whatabout_23.txt", "w", encoding='utf-8') as output:
        #unique= set(dataset)
        #unique_l=list(unique)
        #for t in dataset[:500]

        for t in whataboutism_rows['Text'].drop_duplicates():

            output.write(str(t)+ "\n\n") 
    with open("C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\datasets\\0_no_whatabout_23.txt", "w", encoding='utf-8') as output:
        #unique= set(dataset)
        #unique_l=list(unique)
        #for t in dataset[:500]:
        for t in non_whataboutism_rows['Text'].drop_duplicates()[:500]:
            
            output.write(str(t)+ "\n\n") 


if __name__ == "__main__":
    main()

'''

import pandas as pd
import os

articles_dev = 'C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\SemEval_23_en\\en\\dev-labels-subtask-3'
txt_files = []
label_files = []

def read_labels_file(labels_file_path):
    with open(labels_file_path, 'r', encoding='utf-8') as labels_file:
        lines = labels_file.readlines()
        cleaned_lines = [line.strip() for line in lines]
        return cleaned_lines

def read_text_file(text_file_path, start_position, end_position):
    with open(text_file_path, 'rb', encoding='utf-8') as text_file:
        text_file.seek(start_position)
        try:
            text = text_file.read((end_position) - (start_position)).decode('utf-8', errors='replace')
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError in file {text_file_path}: {e}")
            text = "not_decoded"  # Handle the error by assigning an empty string or any other suitable value
        return text

def main():
    labels_df = pd.DataFrame(columns=['ID', 'Line', 'Labels'])

    for filename in os.listdir(articles_dev):
        f = os.path.join(articles_dev, filename)
        if os.path.isfile(f):
            f = str(f).replace('\\', '/')
            if f.endswith('.txt'):
                label_files.append(str(f))
            elif f.endswith('.template'):
                txt_files.append(str(f))

    for text in label_files:
        # Read the line from the labels file
        labels_line = read_labels_file(text)
        for line in labels_line: 
            l = line.split('\t')
            if len(l) >= 3:
                # Assuming your file is tab-separated
                file_path = text
                df = pd.read_csv(file_path, sep='\t', header=None, names=['ID', 'Line', 'Labels'], on_bad_lines='skip')

                # Display the DataFrame
                labels_df = pd.concat([labels_df, df])

    ids = list(labels_df['ID'])
    id = []
    lines = []
    texts = []

    for text in txt_files:
        # Read the line from the labels file
        t_line = read_labels_file(text)
        for line in t_line: 
            l = line.split('\t')
            id.append(int(l[0]))
            lines.append(l[1])
            texts.append(l[2])

    lines = pd.Series(lines)
    id = pd.Series(id)
    texts = pd.Series(texts)
    data = {'ID': id, 'Line': lines, 'Text': texts}
    d = pd.concat(data, axis=1)

    all_data = pd.merge(labels_df, d, on='ID')
    
    # Filter rows where 'Whataboutism' is not present in the 'Labels' column
    non_whataboutism_rows = all_data[~all_data['Labels'].str.contains('Whataboutism', na=False)]

    # Separate dataframe with only 'Whataboutism' rows
    whataboutism_rows = all_data[all_data['Labels'].str.contains('Whataboutism', na=False)]

    with open("C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\datasets\\0_my_whatabout_23.txt", "w", encoding='utf-8') as output:
        for t in whataboutism_rows['Text'].drop_duplicates():
            output.write(str(t) + "\n\n") 

    with open("C:\\Users\\lored\\OneDrive\\Desktop\\whatabout_research\\datasets\\0_no_whatabout_23.txt", "w", encoding='utf-8') as output:
        for t in non_whataboutism_rows['Text'].drop_duplicates()[:500]:
            output.write(str(t) + "\n\n") 

if __name__ == "__main__":
    main()
