# Words-with-given-letters-in-given-positions
Implementation of a dictionary that allows us to find all the words with a given letter in a given position.


Looking for a word in a dictionary is easy since words are sorted alphabetically. But what if we are looking for all the words where the second letter is a specific one, for example the letter 'c'? Then it's impossible to find all these words unless we sort all the words by their second letter. In this case, we would need a different dictionary for each letter position. In this programme we design a kind of dictionary that allows to find all the words with a given letter in a given position.

Example: (d for our data structure that we will use for this problem, words represent a sample of words from a dictionary)

words = ['class', 'case', 'course', 'dictionary', 'java', 'list', 'program', 'python', 'tuple', 'word']

w = words_letter_position(d, 'a', 1)

print ("result=",w)

output: result= ['case', 'java']

 w = words_letter_position(d, 't', 3)

print ("result=",w)

output: result=['dictionary', 'list']



In my solution that you can see in the .py file I am using a dictionary, as I considered it to be faster than a list. It is more efficient and faster, since the program runs, creates small dictionaries and searches according to the keys, which are the positions of the letters inside the words. Thus, the program does not have to search the whole list of words to find those that have a given letter in a given position, but instead it searches only through the keys of each word, which are the positions of the letters. It finds which word has in the specified position the specified given letter.
