#load dependencies
import os   

#load RegEx
import re   

#Import mean from statistics 
from statistics import mean 



#set variable with path to source file
read_file_path = os.path.join('raw_data','paragraph_1.txt')   

#define word count variable and set initial value
word_count = 0   

#defie sentence_count variable and set initial value
sentence_count = 0   

#create empty list to record count of each word in source
word_char_counts = []   

#create an empty list to record the word count for each sentence in source file
sentence_word_counts = []   


#open source file
with open(read_file_path, 'r') as text_file:
    
    #set variable for contents of source file
    text_source = text_file.read()   
    
    
    #set variable for RegEx compile function 
    word_pattern = re.compile(r'\w+')   
    
    #set variable for RegEx compile function to identify sentences.
    sentence_pattern = re.compile(r'(?<=[a-z][.!?])\W+')   
    
    #set variable for RegEx search for single non-whitespace character
    character_pattern = re.compile(r'\w')   
    
    
    #for sentences in source file split contents of file on 1 or more blank spaces if at least 1 non-whitespace is found add to word count
    for i in re.split(r' +', text_source):   
               if word_pattern.search(i):  
                word_count += 1   
                
                 #Find all non-whitespace characters in word, return into tuple, and append tuple length into list
                word_char_counts.append(len(character_pattern.findall(i)))   
    
    
    #split source file when [.!?] and a space is found; add one to senetencecount
    for i in re.split(sentence_pattern, text_source):   
        sentence_count += 1   
        
        #Find all sentences of non-whitespace characters, return into tuple, and append tuple length into array
        sentence_word_counts.append(len(word_pattern.findall(i)))   
    
    
    #Print
    print(f'Word Count:  {word_count}')   
    
    print(f'Sentence Count:  {sentence_count}')   
    
    print(f'Average Characters per Word:  {round(mean(word_char_counts))}')   
    
    print(f'Average Words per Sentence:  {round(mean(sentence_word_counts))}')  