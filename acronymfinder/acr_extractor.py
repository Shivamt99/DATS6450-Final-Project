# Import necessary libraries
# Using TreebankWordTokenizer

import re
import numpy as np
import nltk.data
from os import listdir
from os.path import isfile, join
from nltk.util import bigrams 
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
treebank_tokenizer = TreebankWordTokenizer()

#load the filenames in a list
dir_base = "../data"
files_list = listdir(dir_base)

#create dictionary to store acronym and it's respective document
dictionary_acronyms = {}
acronym_doc_num = {}

#this function will read all the files in the directory
for num, val in enumerate(files_list):
    input_text = open(dir_base + val, encoding = "utf-8").read()
    
    #regex pattern to find the acronyms in the documents
    acronym = re.findall(r'\([A-Z][A-Z][A-Z]+\)', input_text)
    print(acronym)
    
