#Question: easy
#International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#For convenience, the full table for the 26 letters of the English alphabet is given below:
#[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.
#Return the number of different transformations among all words we have.
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = {"".join(MORSE[ord(c) -  ord('a')] for c in word) for word in words}
        print(seen)
        return len(seen)

words = ["gin", "zen", "gig", "msg"]
result = Solution()
len_word = result.uniqueMorseRepresentations(words)
print('Length of word:', len_word)