#This is my more efficient solution for Problem 1, in which I am using dictionary.
#I am using the list of words from the example of the Problem 1.
#My written solutions and notes for Problem 1 can be found in the PDF file.

import timeit
code_to_test = """
words = ['class', 'dictionary', 'case', 'course', 'java', 'list', 'program', 'python', 'tuple', 'word']
letter = str(input("Enter the letter that you want to search by: "))
position = int(input("Give the position of that letter: "))

def words_letter_position(struct, letter, position):
    new_list = []
    for word in struct:
        dictio = {}
        pos = 0
        for let in word:
            dictio[pos] = let
            pos += 1
        if dictio[position] == letter:
            new_list.append(word)
    return new_list

w = words_letter_position(words, letter, position)
print("result=",w)
"""
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)