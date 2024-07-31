#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int score(string user);
string lower_name(string name);
int main(void)
{
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");
    player_1 = lower_name(player_1);
    player_2 = lower_name(player_2);
    printf("%s\n", player_1);
    printf("%s\n", player_2);
    int score_1 = score(player_1);
    int score_2 = score(player_2);
    printf("%i\n",score_1);
    printf("%i\n",score_2);
    if (score_1 > score_2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score_1 < score_2)
    {
        printf("Player 2 wins\n");
    }
    else if (score_1 == score_2)
    {
        printf("Tie!\n");
    }
    else
    {
        printf("Something went wrong\n");
    }
}
int length(string score){
    int n = 0;
    while (score[n] != '\0')
    {
        n++;
    }
    return n;
}

string lower_name(string name)
{
    // string new = "";
    for (int i = 0, n = length(name); i < n; i++)
    {   if (isupper(name[i]))
        {
            // new += tolower(name[i]);
            name[i] = tolower(name[i]);
        }
    }
    // printf("%s", name);
    return name;
}
int score(string user)
{
    string score_1 = "aeilrustno";
    string score_2 = "dg";
    string score_3 = "bcmp";
    string score_4 = "fhvwy";
    string score_5 = "k";
    string score_6 = "jx";
    string score_7 = "zq";

    int final_score = 0;
    // return 0;
    int user_length = length(user);

        for (int j = 0; j < length(score_1); j++)
        { for (int i = 0; i < user_length ; i++)
        {
            if(user[i] == score_1[j])
            {
                final_score ++;
            }
        }
        }
        for (int j = 0; j < length(score_2); j++)
        {
            for (int i = 0; i < user_length ; i++)
            {
            if(user[i]  == score_2[j])
            {
                final_score = final_score + 2;
            }
        }
        }

        for (int j = 0; j < length(score_3); j++)
        { for (int i = 0; i < user_length ; i++)
    {
            if(user[i] == score_3[j])
            {
                final_score = final_score + 3;
            }
        }
        }
        for (int j = 0; j < length(score_4); j++)
        {for (int i = 0; i < user_length ; i++)
    {
            if(user[i]  == score_4[j])
            {
                final_score = final_score + 4;
            }
        }
        }
        for (int j = 0; j < length(score_5); j++)
        { for (int i = 0; i < user_length ; i++)
    {
            if(user[i]  == score_5[j])
            {
                final_score = final_score + 5;
            }
        }
        }
        for (int j = 0; j < length(score_3); j++)
        { for (int i = 0; i < user_length ; i++)
    {
            if(user[i] == score_6[j])
            {
                final_score = final_score + 8;
            }
        }
        }
        for (int j = 0; j < length(score_7); j++)
        { for (int i = 0; i < user_length ; i++)
    {
            if(user[i] == score_7[j])
            {
                final_score = final_score + 10;
            }
        }
    }
    return final_score;
}
