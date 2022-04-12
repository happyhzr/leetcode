#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isBalanced(struct TreeNode *);
int depth(struct TreeNode *);

bool isBalanced(struct TreeNode *root)
{
    if (root == NULL)
    {
        return true;
    }
    int l = depth(root->left);
    int r = depth(root->right);
    return isBalanced(root->left) && isBalanced(root->right) && abs(l - r) <= 1;
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
    struct TreeNode *t1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t1->val = 3;
    t1->left = NULL;
    t1->right = NULL;
    struct TreeNode *t2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t1->val = 9;
    t1->left = NULL;
    t1->right = NULL;
    struct TreeNode *t3 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t1->val = 20;
    t1->left = NULL;
    t1->right = NULL;
    struct TreeNode *t4 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t1->val = 15;
    t1->left = NULL;
    t1->right = NULL;
    struct TreeNode *t5 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    t1->val = 7;
    t1->left = NULL;
    t1->right = NULL;
    t1->left = t2;
    t1->right = t3;
    t3->left = t4;
    t3->right = t5;
    printf("%d\n", isBalanced(t1));
    return 0;
}