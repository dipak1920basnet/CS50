//Include the necessary library
#include <stdio.h>
#include <cs50.h>

//Declaring a protype of a function
void check_validity(string credit_numb, int count);
int check_length(long credit_number);
int main(void)
{
    while (1)
    {
        // Getting the user_credit number
        long credit_number = get_long("Number ");
        int n = check_length(credit_number);
        if (n == 13 || n == 15 || n == 16)
        {
            string credit_numb = (string)credit_number;
            check_validity(credit_numb,n);
        }
        else
        {
            printf("Invalid");
            break;
        }
    }
}

// Making a check_length() function
int check_length(long credit_number)
{
    int count = 0;
    while (credit_number != 0)
    {
        credit_number /= 10;
        count++;
    }
    return count;

}

// Making a check_validity() function
void check_validity(string credit_numb, int count)
{
    // string change = (string)credit_number;
    for (int i =0 ; i < count; i = i+2)
    {
        printf("%c", credit_numb[i]);
    }
    // return "Invalid";

}


