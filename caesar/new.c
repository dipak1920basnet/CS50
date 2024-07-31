#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

//     // int like = (122-'a'+1)%26+'a';
//     // char tits = (char)like;
//     // printf("%c\n", tits);

    string hello = get_string("Name: ");
    char new[strlen(hello)];
    printf("%s\n",hello);
    // printf("%c\n", tits);
    for (int i = 0, n = strlen(hello); i < n; i++)
    {
        int like = (hello[i]-'a'+1)%26+'a';
        char tits = (char)like;
        new[i] = tits;
        printf("%c\n",new[i]);
    }
    printf("%s\n", new);
}

// {
//     string hello = get_string("Name: ");
//     char new[strlen(hello)];  // Corrected: Changed `string` to `char` array
//     printf("%s\n", hello);

//     for (int i = 0, n = strlen(hello); i < n; i++)
//     {
//         int like = (hello[i] - 'a' + 1) % 26 + 'a';
//         char tits = (char)like;  // Declared and defined `tits` as a variable
//         new[i] = tits;
//         printf("%c\n", new[i]);  // Corrected: Changed `%s` to `%c` for individual characters
//     }

//     return 0;
// }
