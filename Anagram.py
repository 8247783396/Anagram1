""" Anagram Grouping

You are given a list of words. Your task is to group the words into sets of anagrams. Anagrams are words that have the same characters but in a different order.

Write a function that takes the list of words as input and returns a list of sets, where each set contains words that are anagrams of each other.

For example, given the following list of words: ["cat", "dog", "tac", "god", "act"], the function should return: [["cat", "tac", "act"], ["dog", "god"]].

"""


words = input()
words = words.split()
words = set(words)

d = {}

for word in words:

    sorted_word = sorted(word)
    joined_sorted_word = "".join(sorted_word)

    if joined_sorted_word not in d:
        d[joined_sorted_word] = [word]
        
    else:
        d[joined_sorted_word].append(word)

values = list(d.values())
print(values)