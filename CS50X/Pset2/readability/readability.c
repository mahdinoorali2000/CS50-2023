#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int Readability(int, string);

int main(void)
{
    // get & print
    string text = get_string("Text: ");
    int n = strlen(text);
    int index = Readability(n, text);
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int Readability(int n, string text)
{
    float l = 0;
    float s = 0;
    float w = 1;
    // The number of letters, words and sentences
    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]))
        {
            l++;
        }
        if (text[i] == ' ')
        {
            w++;
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            s++;
        }
    }
    // 100
    float L = 100 * (l / w);
    float S = 100 * (s / w);
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    return index;
}