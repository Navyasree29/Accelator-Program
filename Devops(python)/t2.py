"""Task 2: String & List Analyzer 
Problem: 
 Take a sentence as input. Example: "Python is great for DevOps" 
 Do the following: 
1. Count the number of words in the sentence. 
2. Convert the sentence into a list of words and print the list. 
3. Reverse the sentence word by word. Example: "DevOps for great is Python" 
4. Store each word’s length in a tuple. Example: ("Python":6, "is":2, "great":5, ...) 
Concepts Used: 
 Variables & Assignments 
 Strings (splitting, reversing) 
 Lists (word storage) 
 Tuples (word lengths) 
 Dictionary (word: length mapping)"""

sentence = input("Enter a sentence: ")

words = sentence.split()
print("Number of words:", len(words))

print("List of words:", words)

reversed_sentence = " ".join(words[::-1])
print("Reversed sentence:", reversed_sentence)

word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)
