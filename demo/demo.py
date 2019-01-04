"""this file will demonstrate the working of our code. 
   Once executed, the csv file containing the acronyms,
   their full-form and the document number of each acronym
   will be saved in the present working directory"""

from acronymfinder.acr_extractor import AcronymFinder

test = AcronymFinder("../data/")
test.find_print_acronym()


