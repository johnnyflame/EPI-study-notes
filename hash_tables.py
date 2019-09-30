import collections

"""

Hash table practice

EPI chapter 12

"""





"""
Anagrams

"""



def find_anagrams(dictionary):
    sorted_string_to_anagram = collections.defaultdict(list)

    for s in dictionary:
        sorted_string_to_anagram["".join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagram.values() if len(group) >= 2]





"""

12.1 Test for Palindromic Permutations

Description: 

How do we know if a string a string is a palindrome? 

Approach: 

Check that at most one character in the string appears an odd number of times.

Library container used: Counter


"""

def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


"""
12.2
Construct anonymous letter

"""
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Compute frequencies for all chars in letter_text
    char_freq_for_letter = collections.Counter(letter_text)

    # Check if characters in magazine_text can cover characters in
    # char_frequency_for_letter

    for c in magazine_text:
        if c in char_freq_for_letter:
            char_freq_for_letter[c] -= 1
            if char_freq_for_letter[c] == 0:
                del char_freq_for_letter[c]
                if not char_freq_for_letter:
                    return True

    return not char_freq_for_letter


def construct_letter_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))



"""
12.3

Implement an ISBN cache

"""

class LRUCache:
    def __init__(self,capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self,isbn):
        if isbn not in self._isbn_price_table:
            return -1

        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price



    def insert(self,isbn,price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)

        self._isbn_price_table[isbn] = price

    def erase(self,isbn):
        return self._isbn_price_table.pop(isbn,None) is not None


"""
12.4

Compute the LCA, optimizing for close ancestors

    

"""

pass



"""
12.5

"""

def find_nearest_repetition(paragraph):
    word_to_latest_index, nearest_repeated_distance = {}, float('inf')

    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - latest_equal_word)

        word_to_latest_index[word] = i

    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1
