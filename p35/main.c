#include <stdio.h>
#include <assert.h>

int searchInsert(int *nums, int numsSize, int target);
int test();

int main()
{
    test();
    return 0;
}

int searchInsert(int *nums, int numsSize, int target)
{
    int left = 0;
    int right = numsSize - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return left;
}

int test()
{
    int nums1[] = {1, 3, 5, 6};
    assert(searchInsert(nums1, 4, 5) == 2);
    int nums2[] = {1, 3, 5, 6};
    assert(searchInsert(nums2, 4, 2) == 1);
    int nums3[] = {1, 3, 5, 6};
    assert(searchInsert(nums3, 4, 7) == 4);
}
