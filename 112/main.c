#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool hasPathSum(struct TreeNode *, int);
struct TreeNode *newTreeNode(int);

bool hasPathSum(struct TreeNode *root, int targetSum)
{
    if (root == NULL)
    {
        return false;
    }
    if (root->left == NULL && root->right == NULL)
    {
        return root->val == targetSum;
    }
    return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
}

struct TreeNode *newTreeNode(int value)
{
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->left = NULL;
    node->right = NULL;
    node->val = value;
    return node;
}

int main()
{
    struct TreeNode *t1 = newTreeNode(1);
    struct TreeNode *t2 = newTreeNode(2);
    t1->left = t2;
    printf("%d\n", hasPathSum(t1, 1));
    free(t1);
    free(t2);
    return 0;
}