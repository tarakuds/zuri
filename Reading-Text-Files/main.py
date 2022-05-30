# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here     
    fileOpen = open("c:/Users/John's Love/Documents/Zuri/PythonProject1/Reading-Text-Files/testing.txt", "r")
   
    viewFile = fileOpen.read()
    fileOpen.close()
    print(viewFile)
        
    return "Hello World"

read_file_content('testing.txt')   


def count_words():
    text = read_file_content("./testing.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}