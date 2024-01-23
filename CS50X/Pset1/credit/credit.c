#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Enter Card Number
    long n = get_long("Number: ");

    long count = n;
    int i;
    //Count the number of digits
    for (i = 0; count > 0; i++)
    {
        count = count / 10;
    }

    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    long test = n;
    long c = n;
    int sum1 = 0;
    int sum2 = 0;
    int sum3 = 0;
    int mod1 = 0;
    int mod2 = 0;
    int x1 = 0;
    int x2 = 0;
    //Luhn’s Algorithm
    do
    {
        //Separate figures
        mod1 = c % 10;
        c /= 10;
        sum1 += mod1;
        //After the first digit, the rest of the digits are multiplied by two
        mod2 = 2 * (c % 10);
        c /= 10;
        //When the answer is two-digit multiplication, the digits must be separated and added again
        x1 = mod2 % 10;
        x2 = mod2 / 10;
        sum2 += x1 + x2;

    }
    while (c > 0);
    //Total figures
    sum3 = sum1 + sum2;
    //Checking Card
    if (sum3 % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    //Check
    if (i == 15)
    {
        test /= 10000000000000;
        if (test != 34 && test != 37)
        {
            printf("INVALID\n");
            return 0;
        }
        else
        {
            printf("AMEX\n");
            return 0;
        }
    }
    //Check
    if (i == 13)
    {
        test /= 1000000000000;
        if (test != 4)
        {
            printf("INVALID\n");
            return 0;
        }
        else
        {
            printf("VISA\n");
            return 0;
        }
    }
    //Check
    if (i == 16)
    {
        test /= 100000000000000;
        if (test == 51 || test == 52 || test == 53 || test == 54 || test == 55)
        {
            printf("MASTERCARD\n");
            return 0;
        }
        else
        {
            test /= 10;
            if (test == 4)
            {
                printf("VISA\n");
                return 0;
            }
            else
            {
                printf("INVALID\n");
                return 0;
            }
        }
    }

}