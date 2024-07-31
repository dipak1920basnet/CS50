vowels = ['a','e','i','o','u']
get_word = input("Input: ")
new_word = ''
for i in get_word:
    if i.lower() in vowels:
        continue
    else:
        new_word += i
print(new_word)
