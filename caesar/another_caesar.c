// This code is a complete failure


#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>

string cipher_text(string plain_text);
int main(int argc, string argv[])
{
    int key = atoi(argv[1]);
    if (argc == 2) // checks if length of command line arguments and if it is not equal to 2 then it will return 1.
    {
        if(argv[1] == key) // checks if command line is integer or not
    {
        if (key < 0 || key >25)
        {
            printf("Error occured::"); // prints error if command line argument is negative integer
            return 1;
        }
        else
        {
        string plain_text = get_string("plaintext: ");
        string k = cipher_text(plain_text);
        printf("plaintext: %s\n",k);
        return 0;
        }

    }
    else {
        printf("The error occured");
        return 1;
    }

    }
    else
    {
        printf("Error occured\n");
        return 1;
    }
}

string cipher_text(string plain_text)
{
    return plain_text;
}
