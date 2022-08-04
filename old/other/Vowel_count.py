vowels=["a", "e", "i", "o", "u"]
print("Vowels in words counter")
word = input("Input a word: ")

counter=0

for letter in word:
    for letter_v in vowels:
        if letter==letter_v:
            counter+=1

print(counter)