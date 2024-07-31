#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string name = get_string("Name: ");
    // name = tolower(name);
    // string new = "";
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        // string new += tolower(name[i]);
        printf("%c",tolower(name[i]));
    }
    printf("\n");

}
