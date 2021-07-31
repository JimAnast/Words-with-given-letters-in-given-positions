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
