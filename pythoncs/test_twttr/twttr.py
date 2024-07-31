def main():
    get_word = str(input("Input: "))
    shorten(get_word)
def shorten(word):
    vowels = ['a','e','i','o','u']
    new_word = ''
    for i in word:
        if i.lower() in vowels:
            continue
        else:
            new_word += i
    return new_word

if __name__ == "__main__":
    main()
