# Import necessary libraries
# Using TreebankWordTokenizer

import re
import numpy as np
import nltk.data
from os import listdir
from os.path import isfile, join
from nltk.util import bigrams 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
import pandas as pd
from acronymfinder import get_acronym
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
treebank_tokenizer = TreebankWordTokenizer()
stopWords = set(stopwords.words('english'))
stopWords.remove("of")
stopWords.remove("to")


class AcronymFinder:
    def __init__(self, path):
        self.path = path
        
    def find_print_acronym(self):
        files_list = listdir(self.path)
        dictionary_acronyms = {}
        acronym_doc_num = {}
        
        # Read all the files in the directory and store data in a list one by one by file.
        for num, val in enumerate(files_list):
            input_text = open(self.path + val, encoding = "utf-8").read()
    
        # Regex Pattern
            acronym = re.findall(r'\([A-Z][A-Za-z\.][A-Z]+\)', input_text)
            acronym_list = []
            for a in acronym:
                sample = list(a)
                sample.remove('(')
                sample.remove(')')
                acronym_list.append("".join(sample))
    
        # Read the text data and tokenize it first by sentence then by word in that sentence.
            sentence_tokens = sentence_tokenizer.tokenize(input_text)
            sentences = [treebank_tokenizer.tokenize(sentence) for sentence in sentence_tokens]
            for sentence in sentences:
                sentence1 = [words for words in sentence if words not in stopWords]
                for words in sentence1:
                    for acr in acronym_list:
                        if acr in sentence1:
                            acronym_sent = acr
                            if (acronym_sent not in list(dictionary_acronyms.keys())):
                                dictionary_acronyms[acronym_sent] = get_acronym.strip_acronym(acronym_sent, sentence1)
                                acronym_doc_num[acronym_sent] = num+1
                                
        # Define and Map the dictionary                        
        final_dict = {"Acronym" : [], "Full-form" : [], "Document-number" : []}
        acr_list = [key for key, value in dictionary_acronyms.items()]
        for acronym in acr_list:
            final_dict["Acronym"].append(acronym)
            final_dict["Full-form"].append(dictionary_acronyms[acronym])
            final_dict["Document-number"].append(acronym_doc_num[acronym])
            
        # Save as dataframe and output a csv    
        df = pd.DataFrame(final_dict)
        df.to_csv('Final_dictionary.csv')
        
