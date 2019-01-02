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
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
treebank_tokenizer = TreebankWordTokenizer()
stopWords = set(stopwords.words('english'))

#load the filenames in a list
dir_base = "../data/"
files_list = listdir(dir_base)

#create dictionary to store acronym and it's respective document
dictionary_acronyms = {}
acronym_doc_num = {}

#this function will read all the files in the directory
for num, val in enumerate(files_list):
    input_text = open(dir_base + val, encoding = "utf-8").read()
    
    #regex pattern to find the acronyms in the documents
    acronym = re.findall(r'\([A-Z][A-Za-z\.][A-Z]+\)', input_text)
    acronym_list = []
    for a in acronym:
        sample = list(a)
        sample.remove('(')
        sample.remove(')')
        acronym_list.append("".join(sample))
        
    #this function will read the text data and tokenize it first by sentence then by word in that sentence.        
        
    sentence_tokens = sentence_tokenizer.tokenize(input_text)
    sentences = [treebank_tokenizer.tokenize(sentence) for sentence in sentence_tokens]
    for sentence in sentences:
        sentence1 = [words for words in sentence if words not in stopWords]
        for words in sentence1:
            for acr in acronym_list:
                if acr in sentence1:
                    acronym_sent = acr
                    if (acronym_sent not in list(dictionary_acronyms.keys())):
                        dictionary_acronyms[acronym_sent] = get_acronym(acronym_sent, sentence1)
                        acronym_doc_num[acronym_sent] = num+1 
