# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input('Input the first word to compare :- ')
anagram = input('Input the first word to compare :- ')

def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = word.lower()
    anagram = anagram.lower()

    if(len(word) == len(anagram)):
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

        
        if(sorted_word == sorted_anagram):
            print("True " + word + " and " + anagram + " are anagram.")
        else:
            print("False " + word + " and " + anagram + " have same word length but are not anagram.")
        return True

    else:
        print("False " + word + " and " + anagram + " are not anagram.")

        return False

find_anagram(word, anagram)

