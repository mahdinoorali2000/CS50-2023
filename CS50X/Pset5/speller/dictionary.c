// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100000;
int DICT_S;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *n = table[hash(word)];
    while (n != NULL)
    {
        if (strcasecmp(n->word, word) == 0)
        {
            return true;
        }
        n = n->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int x = 0;
    int len = strlen(word);
    for (int z = 0; z < len; z++)
    {
        x = (x * 51) + (toupper(word[z]) - 'A');
    }

    return x % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *DICT = fopen(dictionary, "r");
    if (DICT == NULL)
    {
        printf("could not open %s\n", dictionary);
        return false;
    }
    char kalame[LENGTH + 1];
    while (fscanf(DICT, "%s", kalame) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, kalame);
        int hash_n = hash(kalame);
        n->next = table[hash_n];
        table[hash_n] = n;
        DICT_S++;
    }
    fclose(DICT);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return DICT_S;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int x = 0; x < N; x++)
    {
        node *n = table[x];
        while (n != NULL)
        {
            node *m = n;
            n = n->next;
            free(m);
        }
        if (n == NULL && x == (N - 1))
        {
            return true;
        }
    }
    return false;
}
