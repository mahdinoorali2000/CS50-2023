#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Receive input from the user
    string name = get_string("What's your name? ");
    //Print hello user
    printf("hello, %s\n", name);
}