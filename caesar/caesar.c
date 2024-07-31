#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void cipher_text(string plain_text, int key);
int check_alpha(string one);
int main(int argc, string argv[])
{
    if (argc != 2) // handles if argc length is less than or greater than 2
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        int apha = check_alpha(argv[1]);
        if (apha == 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            int key = atoi(argv[1]);
            string plain_text = get_string("plaintext: ");
            cipher_text(plain_text, key);
            return 0;
        }
    }
}

// Checks if argv[1] is alpha or not
int check_alpha(string one)
{
    for (int i = 0; i < strlen(one); i++)
    {
        if (isalpha(one[i]) != 0)
        {
            return 0;
        }
    }
    return 1;
}

// a function to change the plain text to cipher text.
void cipher_text(string plain_text, int key)
{
    int cipher_len = strlen(plain_text);
    char cipher[cipher_len];
    for (int j = 0; j < strlen(plain_text); j++)
    {
        if (isupper(plain_text[j]) != 0) // For upper case alphabets
        {
            if ((plain_text[j] + key) > 90)
            {
                int like = (plain_text[j] - 'A' + key) % 26 +
                           'A'; // rounds up the value if value crosses Z
                char tost = (char) like;
                cipher[j] = tost;
            }
            else
            {
                cipher[j] = (char) plain_text[j] + key;
            }
        }
        else if ((islower(plain_text[j]) != 0)) // For lowercase alphabets
        {
            if ((plain_text[j] + key) > 122)
            {
                int like = (plain_text[j] - 'a' + key) % 26 +
                           'a'; // rounds up the value if value crosses z
                char tost = (char) like;
                cipher[j] = tost;
            }
            else
            {
                cipher[j] = (char) (plain_text[j] + key);
            }
        }
        else
        {
            cipher[j] = plain_text[j];
        }
    }
    printf("ciphertext: %s\n", cipher);
}
