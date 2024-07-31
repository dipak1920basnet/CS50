#include <stdio.h>
#include <cs50.h>
int main(void)
{   int x = 1;
    while (x==1)
    {
        int number = get_int("Height: ");
       if (8>=number && number >= 1)
       {
         for(int j = 0; j < number; j++)
    {
        for(int i = number-1 ; i-j > 0; i--)
    {
        printf(" ");
    }
    for (int k = 0; k<=j; k++){
        printf("#");
       }
    // printf("#");
    printf("  ");
    for (int k = 0; k<=j; k++){
        printf("#");
       }
    printf("\n");
    }
       }
       else
       {
        continue;
       }
       x = 0;
    }
}
