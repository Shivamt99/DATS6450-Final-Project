# DATS6450-Final-Project
**Acronym_Finder**

This is a package to extract acronyms found in text/data and identify the mapping of the acronym to the words it stands for(full form of the acronym) and also the document number it occured in.
The data we used here is to demostrate how the code works and to show the desired output.

**Package Attributes**

- Loading all the data file into a directory
- Extracting the Acronyms from the data
- Creating a dictionary having Acronym, its full form and the document number it occurs in.
- An output in form of a csv file with "Acronym", "Full form", "document number" 

A demo.py file in demo folder to demonstrate the working of our code and the output that will be saved in the present working directory.

**Code Logic**

Usually there’s a pattern in most of the data/text that most of the Acronyms are mentioned inside brackets “( )” preceded by its full form. So, the best approach was to form a regex to extract those acronyms which are inside the brackets. So, we looked at the immediate tokenized sentences where the acronyms are found.

Then we took single words of acronyms and broke it into a list of characters. Set its index to 0 and then formed a loop that will iterate through the indices of the tokens in the sentence tokens of our corpus. The logic is the compare the indexes of the tokenized Acronym list words with the tokenized corpus list words. “if(str.lower(sentence[i][0]) == str.lower(acronym[0])):” then we look further to the next Tokenized word in the sentence to compare it with the next character of the acronym word till “(index<length_acronym)”. We give two flags, True and false.

We kept saving the acronyms list compared and found in a dictionary and gave the condition as to when it iterates through the acronym list to compare it with the corpus of tokenized words, it searches through the dictionary of acronyms list words first so that if it is present in the dictionary already then it need not search it again. This saves a hell lot of time and computation power, essentially optimizing the code and search process.

Then we printed out the dictionary which contained Acronyms and its mapped full form, but I saw some of the acronyms did not have their full forms mapped instead it showed “none”. For eg (ACSA) Acquisition and Cross-Servicing Agreement, (AGATRS) Automated Tracking and Reporting System. These words had “and” in their full forms which means I needed to remove the stop words too. So, we went back and removed the stop words in the tokenized corpus file words, which essentially made mapping way better. 

Finally we formed another loop to print in the file number (Document_number) associated where the acronyms were found, along with the full forms and then wrote a function to output it as a csv file.

**Installation**

This repository can be found at the address below. You can clone or download this repository by going to the link.

'''
https://github.com/darshan22/DATS6450-Final-Project.git
'''



