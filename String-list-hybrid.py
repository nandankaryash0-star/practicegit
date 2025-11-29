# String & list hybrid

sentence = input("Write the sentence--  ")

#this will split the words 
words = sentence.split()

#Sort the word alphabetically 
word_sorted = sorted(words)

#longest word
longest = max(words, key=len)

#shortest word 
shortest = min(words, key=len)

print("-----RESULT-----")
print(f"Word (Sorted). {word_sorted}")
print(f"The longest word is {longest}")
print(f"The shortest word is {shortest}")