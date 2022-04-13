#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int minDepth(struct TreeNode *);

int minDepth(struct TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }
    if (root->left == NULL)
    {
        return minDepth(root->right) + 1;
    }
    if (root->right == NULL)
    {
        return minDepth(root->left) + 1;
    }
    int l = minDepth(root->left);
    int r = minDepth(root->right);
    return l < r ? l + 1 : r + 1;
}

int main()
{
    struct TreeNode *t1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t1->left = NULL;
    t1->right = NULL;
    t1->val = 3;
    struct TreeNode *t2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t2->left = NULL;
    t2->right = NULL;
    t2->val = 9;
    struct TreeNode *t3 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t3->left = NULL;
    t3->right = NULL;
    t3->val = 20;
    struct TreeNode *t4 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t4->left = NULL;
    t4->right = NULL;
    t4->val = 15;
    struct TreeNode *t5 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t5->left = NULL;
    t5->right = NULL;
    t5->val = 7;
    t1->left = t2;
    t1->right = t3;
    t3->left = t4;
    t3->right = t5;
    printf("%d\n", minDepth(t1));
    return 0;
}