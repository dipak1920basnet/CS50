// Inport necessary library
#include <stdio.h>
#include <cs50.h>

// Declaring a prototype for function
int count_coin(int change_owed);
int main(void)
{

// Get change owed from the customer
while (1){
    int change_owed = get_int("Change owed: ");
    if (change_owed < 0)
    {
        continue;
    }
    else
    {
        printf("%i\n",count_coin(change_owed));
        break;
    }

}
// Defining a function.
}
int count_coin(int change_owed)
{
    // declare required variable and set their value
    int quarters = 25;
    int dimes = 10;
    int nickles = 5;
    int pennies = 1;
    int count = 0;
    // Check if the change owed is among the variables if so try making the change_owed to zero and add one to count
    // if (change_owed == quarters || change_owed == dimes || change_owed == nickles || change_owed == pennies)
    // {
    //     count ++;
    //     return count;
    // }

    // Run while loop until change_owed is not equal to zero
    while (change_owed != 0)
    {
        // printf("%i\n",change_owed);
    if (change_owed <= 0)
    {
        break;
    }
        // if not try to minimize the change owed and add one to count
        if (change_owed >= quarters)
        {
            change_owed -= quarters;
            count++;
        }
        else if (change_owed >= dimes)
        {
            change_owed -= dimes;
            count++;
        }
        else if (change_owed >= nickles)
        {
            change_owed -= nickles;
            count++;
        }
        else if (change_owed >= pennies)
        {
            change_owed -= pennies;
            count++;
        }

    }
// When finally change owed is zero return count
    return count;
}

