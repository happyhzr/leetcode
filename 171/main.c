#include <stdio.h>
#include <string.h>

#define N 8

int titleToNumber(char *);

int titleToNumber(char *columnTitle)
{
    int n = 0;
    int l = strlen(columnTitle);
    for (int i = 0; i < l; i++)
    {
        n = 26 * n + (columnTitle[i] - 'A') + 1;
    }
    return n;
}

int main()
{
    char s[N];
    while (scanf("%s", s) != EOF)
    {
        printf("%d\n", titleToNumber(s));
    }
}