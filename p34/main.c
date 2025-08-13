#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int *searchRange(int *nums, int numsSize, int target, int *returnSize);
int search_left(int *nums, int num_size, int target);
int search_right(int *nums, int num_size, int target);
int test();

int main()
{
    test();
    return 0;
}

int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{
    int left = search_left(nums, numsSize, target);
    int right = search_right(nums, numsSize, target);
    *returnSize = 2;
    int *res = (int *)malloc(sizeof(int) * 2);
    res[0] = left;
    res[1] = right;
    return res;
}

int search_left(int *nums, int num_size, int target)
{
    int left = 0;
    int right = num_size - 1;
    int left_border = -1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
        {
            left_border = mid;
            right = mid - 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return left_border;
}

int search_right(int *nums, int num_size, int target)
{
    int left = 0;
    int right = num_size - 1;
    int right_border = -1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
        {
            right_border = mid;
            left = mid + 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return right_border;
}

int test()
{
    int nums1[] = {5, 7, 7, 8, 8, 10};
    int res_num = 0;
    int *p = &res_num;
    int *res = searchRange(nums1, 6, 8, p);
    assert(res[0] == 3);
    assert(res[1] == 4);
    free(res);
    int nums2[] = {5, 7, 7, 8, 8, 10};
    res = searchRange(nums2, 6, 6, p);
    assert(res[0] == -1);
    assert(res[1] == -1);
    free(res);
    int num3[] = {};
    res = searchRange(num3, 0, 0, p);
    assert(res[0] == -1);
    assert(res[1] == -1);
    free(res);
}