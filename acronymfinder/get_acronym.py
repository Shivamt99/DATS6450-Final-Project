#This module defines a function to extract the acronym from the sentence.

def strip_acronym(acronym, sentence):
    for i in range(len(sentence)):
        if(str.lower(sentence[i][0]) == str.lower(acronym[0])):
            acr = ""
            acr = acr+ sentence[i] + " "
            length_acronym = len(acronym)
            index = 1
            j = i + 1
            acronym_found = True
            while(index<length_acronym):
                if(str.lower(sentence[j][0]) == str.lower(acronym[index])):
                    acr = acr + sentence[j] + " "
                    index = index + 1
                    j = j + 1
                else:
                    acronym_found = False
                    break
            if acronym_found:
                return (acr.strip())

