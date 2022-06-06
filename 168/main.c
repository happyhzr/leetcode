#include <stdio.h>
#include <stdlib.h>

#define N 8

void reverse(char *, int);
char *convertToTitle(int);

void reverse(char *str, int len)
{
    int left = 0;
    int right = len - 1;
    int t;
    while (left < right)
    {
        t = str[left];
        str[left] = str[right];
        str[right] = t;
        left++;
        right--;
    }
}

char *convertToTitle(int columnNumber)
{
    char *str = (char *)malloc(sizeof(char) * N);
    int i = 0;
    while (columnNumber > 0)
    {
        int t = (columnNumber - 1) % 26 + 1;
        str[i] = (t - 1) + 'A';
        i++;
        columnNumber = (columnNumber - t) / 26;
    }
    str[i] = '\0';
    reverse(str, i);
    return str;
}

int main()
{
    int columnNumber;
    while (scanf("%d", &columnNumber) != EOF)
    {
        char *s = convertToTitle(columnNumber);
        printf("%s\n", s);
        free(s);
    }
    return 0;
}