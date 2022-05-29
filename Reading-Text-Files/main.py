# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import os

working_directory = os.getcwd()
print(os.getcwd())

def read_file_content(filename):
    # [assignment] Add your code here 
  file_directory = "c:/Users/John's Love/Documents/Zuri/PythonProject1/Reading-Text-Files/testing.txt"

  file_to_open= open(file_directory, 'r')
  print(file_to_open.read())
  file_to_open.close()
  return file_directory

read_file_content("testing.txt")
    


def count_words():
    text = read_file_content("./testing.txt")
    # [assignment] Add your code here
    # fname = input("Enter file name: ")
    word=input("Enter word to be searched:")
    k = 0
    
    with open(text, 'r') as f:
        for line in f:
          words = line.split()
          for i in words:
              if(i==word):
                  k=k+1
    print("Occurrences of the word: " + str(k))

    return {"as": 10, "would": 20}

count_words()