from cs50 import get_string


def main():
    Texts = get_string("Text: ").lower()
    total_words = count_words(Texts)
    total_sentences = count_sentences(Texts)
    total_letters = count_letters(Texts)
    total_letters = total_letters - total_sentences - (total_words-1)
    average_letters = letter_average(total_letters, total_words)
    average_sentences = sentence_average(total_sentences, total_words)
    readibility = 0.0588 * average_letters - 0.296 * average_sentences - 15.8
    readibility = round(readibility)
    if (readibility < 1):
        print("Before Grade 1")
    elif (readibility >= 16):
        print("Grade 16+")
    else:
        print(f"Grade: {readibility}")


def count_words(x):
    words = 1 + x.count(" ")
    return words


def count_sentences(x):
    sentences = 0
    end = [".", "!", "?"]
    for i in x:
        if i in end:
            sentences += 1
    return sentences


def count_letters(x):
    letters = len(x)
    remove = ["\'", "\"", ","]
    for i in x:
        if i in remove:
            letters -= 1
    return letters


def letter_average(x, y):
    average = (x/y) * 100
    return average


def sentence_average(x, y):
    average = (x/y) * 100
    return average


if __name__ == "__main__":
    main()
