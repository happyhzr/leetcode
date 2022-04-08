#include <stdio.h>
#include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *sortedArrayToBST(int *, int);
int isBst(struct TreeNode *);
int depth(struct TreeNode *);
struct TreeNode *helper(int *, int, int);

struct TreeNode *sortedArrayToBST(int *nums, int numsSize)
{
    return helper(nums, 0, numsSize - 1);
}

struct TreeNode *helper(int *nums, int start, int end)
{
    if (start > end)
    {
        return NULL;
    }
    int mid = (start + end) / 2;
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = nums[mid];
    node->left = helper(nums, start, mid - 1);
    node->right = helper(nums, mid + 1, end);
    return node;
}

int isBst(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 1;
    }
    int l = depth(root->left);
    int r = depth(root->right);
    return abs(l - r) <= 1;
}

int depth(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }
    int l = depth(root->left);
    int r = depth(root->right);
    return l > r ? l + 1 : r + 1;
}

int main()
{
    int nums[] = {-10, -3, 0, 5, 9};
    struct TreeNode *root = sortedArrayToBST(nums, 5);
    printf("%d\n", isBst(root));
    int nums1[] = {1, 3};
    root = sortedArrayToBST(nums1, 2);
    printf("%d\n", isBst(root));
    return 0;
}