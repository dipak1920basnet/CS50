// Note :: This code is a failure and only works for some inputs not all
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int total_words(string text);
int total_sentences(string text);
int total_letter(string text);
int average_letter(int letter, int words);
int average_sentence(int sentence, int words);
float point(float L, float S);
int main(void)
{
    string text = get_string("Text: ");
    int words_number = total_words(text);
    int sentence_number = total_sentences(text);
    int letter_number = total_letter(text);
    // printf("Total letters:: %i\n Words number:: %i\n Total sentences:: %i\n",letter_number, words_number,sentence_number);
    int L = average_letter(letter_number, words_number);
    int S = average_sentence(sentence_number, words_number);
    float score = point(L,S);
    // printf("Average Letter:: %f  Average Sentence:: %f\n",L,S);
    // float score = point(537,4.20);
    if (score > 16)
    {
        printf("Grade %f+ \n",score);
    }
    else if (score < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %f\n",score);
    }
}
int total_words(string text){
    int total_words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' '){
            total_words++;
        }
    }
    return total_words;
}
int total_sentences(string text){
    int total_sentence = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] == '.') || (text[i] == '!') || (text[i] == '?') ){
            total_sentence++;
        }
    }
    return total_sentence;
}
int total_letter(string text)
{
    int total_letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] != ' ') || (text[i] != '.') || (text[i] != '!') || (text[i] != '?'))
        {

            total_letters ++;
        }
    }
    return total_letters;
}

int average_letter(int letter, int words)
{   float check = (float)(letter/words);
    float average = round((check)*100);
    return round(average);
}
int average_sentence(int sentence, int words)
{
    float check = (float)(sentence/words);
    float average = round((check)*100);
    return round(average);
}
float point(float L, float S)
{
    float points = ((0.0588*L)-(0.296*S)-(15.8));
    return (round)(points);
}
