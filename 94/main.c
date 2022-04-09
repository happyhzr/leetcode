#include <stdlib.h>
// Definition for a binary tree node.
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int *inorderTraversal(struct TreeNode *, int *);
void helper(struct TreeNode *, int *, int *);

#define MAX_SIZE 100

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *inorderTraversal(struct TreeNode *root, int *returnSize)
{
    int *a = (int *)calloc(MAX_SIZE, sizeof(int));
    *returnSize = 0;
    helper(root, a, returnSize);
    return a;
}

void helper(struct TreeNode *root, int *a, int *size)
{
    if (root == NULL)
    {
        return;
    }
    helper(root->left, a, size);
    a[(*size)] = root->val;
    (*size)++;
    helper(root->right, a, size);
}

int main()
{
    return 0;
}