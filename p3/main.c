#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define N 128

int lengthOfLongestSubstring(char *s);
void init_set(bool *set, int n);
void remove_set(bool *set, int e);
bool in_set(bool *set, int e);
void add_set(bool *set, int e);

int lengthOfLongestSubstring(char *s)
{
    bool occ[N];
    init_set(occ, N);
    int l = strlen(s);
    int rk = -1;
    int ans = 0;
    for (int i = 0; i < l; i++)
    {
        if (i != 0)
        {
            remove_set(occ, s[i - 1]);
        }
        while (rk + 1 < l && !in_set(occ, s[rk + 1]))
        {
            add_set(occ, s[rk + 1]);
            rk++;
        }
        ans = ans > rk - i + 1 ? ans : rk - i + 1;
    }
    return ans;
}

void init_set(bool *set, int n)
{
    for (int i = 0; i < n; i++)
    {
        set[i] = false;
    }
}

void remove_set(bool *set, int e)
{
    set[e] = false;
}

bool in_set(bool *set, int e)
{
    return set[e];
}

void add_set(bool *set, int e)
{
    set[e] = true;
}

int main()
{
    char *s1 = " ";
    printf("%d\n", lengthOfLongestSubstring(s1));
    char *s2 = "abcabcbb";
    printf("%d\n", lengthOfLongestSubstring(s2));
    char *s3 = "bbbbb";
    printf("%d\n", lengthOfLongestSubstring(s3));
    char *s4 = "pwwkew";
    printf("%d\n", lengthOfLongestSubstring(s4));
    return 0;
}