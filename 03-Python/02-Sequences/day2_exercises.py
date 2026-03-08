# Unordered
text = ('this is sample text with several words '
        'this is more sample text with some different words '
        'that is also another text with other different words'
        )
print("="*50)
print("First Problem:")
print("="*50)

# 1-try to get number of each text in paragraph
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word counts in the text:")
for word, count in word_count.items():
    print(f"{word}: {count}")


print("="*50)
print("Second Problem:")
print("="*50)

# 2-Check Whether a Given Number is Prime or not from 1 to 30
print("The prime numbers in range of (1 and 30) are:")
for num in range(1, 31):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(f"{num}", end=" ")

print("="*50)
print("Third Problem:")
print("="*50)

# Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.
vowels = 'aeiou'
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"\nThe number of vowels in the text is: {vowel_count}")
print("="*50)
print("Fourth Problem:")
print("="*50)

# 4.write program to check whether the string is Symmetrical or Palindrome

input_string = input("Enter a string to check if it's a palindrome: ")  
clean_text = input_string.replace(" ", "").lower()
result = clean_text == clean_text[::-1]
print(f"'{input_string}' is {'a palindrome' if result else 'not a palindrome'}")

print("="*50)
print("Fifth Problem:")
print("="*50)


# 5.write Program to Swap Two Elements in a Lista = [10, 20, 30, 40, 50]
a = [10, 20, 30, 40, 50]
print("Original list:", a)
a[1], a[3] = a[3], a[1]
print("List after swapping:", a)
# ----#
print("="*50)
print("Sixth Problem:")
print("="*50)

# 6.Calculate the sum of all positive numbers in a list ,numbers = [-10, 15, -5, 20, -3, 30]  .
numbers = [-10, 15, -5, 20, -3, 30]
positive_sum = sum(num for num in numbers if num > 0)
print(f"The sum of all positive numbers in the list is: {positive_sum}")
