#include <stdio.h>
#include <limits.h>

int maxProfit(int *, int);

int maxProfit(int *prices, int pricesSize)
{
    int min = INT_MAX;
    int max = 0;
    for (int i = 0; i < pricesSize; i++)
    {
        if (prices[i] < min)
        {
            min = prices[i];
        }
        else if (prices[i] - min > max)
        {
            max = prices[i] - min;
        }
    }
    return max;
}

int main()
{
    int prices1[] = {7, 1, 5, 3, 6, 4};
    printf("%d\n", maxProfit(prices1, 5));
    int prices2[] = {7, 6, 4, 3, 1};
    printf("%d\n", maxProfit(prices2, 5));
    return 0;
}