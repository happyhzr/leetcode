#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int hash[256];

bool isomorphic(char *s, char *t);
bool isIsomorphic(char *s, char *t);

bool isomorphic(char *s, char *t)
{
    memset(hash, -1, sizeof(hash));
    //int i;
    int len = strlen(s);
    for (int i = 0; i < len; i++)
    {
        int n1 = (int)s[i];
        int n2 = (int)t[i];
        if (hash[n1] == -1)
        {
            hash[n1] = n2;
        }
        else
        {
            if (hash[n1] != n2)
            {
                return false;
            }
        }
    }
    return true;
}

bool isIsomorphic(char *s, char *t)
{
    if (isomorphic(s, t) && isomorphic(t, s))
    {
        return true;
    }
    return false;
}

// bool isIsomorphic(char *s, char *t)
// {
//     if (!isomorphic(s, t))
//     {
//         return false;
//     }
//     if (!isomorphic(t, s))
//     {
//         return false;
//     }
//     return true;
// }

int main()
{
    char *s = "egg";
    char *t = "add";
    bool res = isIsomorphic(s, t);
    printf("%d\n", res);
    return 0;
}