# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    
    split_word = []
    split_anagram = []

    for character in word:
        split_word.append(character)
    split_word.sort()
    for character in anagram:
        split_anagram.append(character)
    split_anagram.sort()

    while ' ' in split_word:
        split_word.remove(' ')
    while ' ' in split_anagram:
        split_anagram.remove(' ')
    
    if split_word == split_anagram:
        return True
    else:
        return False


print(find_anagram('New York Times', 'Monkeys write'))

