#include <stdio.h>
#include <assert.h>

int mySqrt(int x);
int test();

int main()
{
    test();
    return 0;
}

int mySqrt(int x)
{
    int l = 0;
    int r = x;
    int ans = 0;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        long t = (long)mid * (long)mid;
        if (t <= x)
        {
            ans = mid;
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
    }
    return ans;
}

int test()
{
    assert(mySqrt(4) == 2);
    assert(mySqrt(8) == 2);
}