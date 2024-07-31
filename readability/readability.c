#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

float average_letter(int letter, int words);
float average_sentence(int sentences, int words);
int calculation(float letters, float sentences);
int main(void)
{
    string text = get_string("Text:");
    int total_words = 1;
    int total_sentences = 0;
    int total_letter = strlen(text);
    int filter_letter = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            total_words ++;
        }
        else if ((text[i] == '.') || (text[i] == '!') || (text[i] == '?') ){
            total_sentences++;
        }
        else if ((text[i] == '\'') || (text[i] == '\"') || (text[i] == ','))
        {
            filter_letter ++;
        }
    }
    // printf("total_letter : %i\n", total_letter);
    // printf("filter_letter: %i\n", filter_letter);
    total_letter = total_letter-((total_words-1)+total_sentences+filter_letter);
    // printf("total_words: %i\n",total_words);
    // printf("total_sentence: %i\n", total_sentences);
    // printf("total_letter: %i\n", total_letter);


    float average_letters = average_letter(total_letter, total_words);
    float average_sentencess = average_sentence(total_sentences, total_words);

    int calculate_points = calculation(average_letters, average_sentencess);
    // printf("average_lettersssssssssssss:: %f\n", average_letters);
    // printf("average_sentencesssssssssss:: %f\n", average_sentencess);
    // printf("Pointssssssssssssssss:: %i\n",calculate_points);

    if (calculate_points < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (calculate_points >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n",calculate_points);
    }
    return 0;
}

float average_letter(int letter, int words)
{
    float calculation = (((float) letter) / ((float) words))*100;
    return calculation;
}

float average_sentence(int sentences, int words)
{
    float calculation = (((float) sentences) / ((float) words))*100;
    return calculation;
}

int calculation(float letters, float sentences)
{
    float points = (0.0588*letters) - (0.296*sentences) -15.8;
    return (round)(points);
}
