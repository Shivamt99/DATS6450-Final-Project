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

**Installation**

This repository can be found at the address below. You can clone or download this repository by going to the link.


```
https://github.com/darshan22/DATS6450-Final-Project.git
```

After you clone/download the repository, to install the package run the following command from the terminal:

```
python setup.py install
```

**Required packages**

Install the required packages by executing the following commands:

```
pip install nltk
pip install pandas
pip install numpy
pip install re
```

After you install the package on your computer, you can navigate to the demo folder in the repository to and execute the `demo.py` file. On executing the file, the csv file will be saved to the current working directory.

