#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Enter height pyramid
    int h;
    do
    {
        h = get_int("Enter heigt: ");
    }
    while (h <= 0 || h >= 9);
    //print pyramid
    for (int i = 1; i <= h; i++)
    {
        //print space
        for (int j = i; j < h; j++)
        {
            printf(" ");
        }
        //print first pyramid
        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }
        //print second pyramid
        printf("  ");
        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}