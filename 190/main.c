#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define N 32

uint32_t reverseBits(uint32_t);

uint32_t reverseBits(uint32_t n)
{
    uint32_t ans = 0;
    for (int i = 0; i < N && n > 0; i++)
    {
        ans = (ans | (n & 1) << (N - 1 - i));
        n = n >> 1;
    }
    return ans;
}

int main()
{
    int n = 0b00000010100101000001111010011100;
    printf("%u\n", reverseBits(n));
    n = 0b11111111111111111111111111111101;
    printf("%u\n", reverseBits(n));
}