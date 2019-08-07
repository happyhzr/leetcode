#include <stdio.h>

void move_nums(int nums[],int nums_size,int start)
{
	for(int i=start;i<nums_size-1;i++)
	{
		nums[i]=nums[i+1];
	}
}

int removeDuplicates(int* nums, int numsSize)
{
	int dup=0;
	for(int i=0;i<numsSize;)
	{
		if(i==0||nums[i-1]!=nums[i])
		{
			dup=1;
			i++;
		}
		else
		{
			dup++;
			if(dup>=3)
			{
				move_nums(nums,numsSize,i);
				numsSize--;
				dup--;
			}
			else
			{
				i++;
			}
		}
		for (int i = 0; i < numsSize; i++) 
		{
    		printf("%d ",nums[i]);
		}
		printf("\n");
	}
	return numsSize;
}

int main()
{
	int nums[] = {0,0,1,1,1,1,2,3,3};

	// nums is passed in by reference. (i.e., without making a copy)
	int len = removeDuplicates(nums,6);

	// any modification to nums in your function would be known by the caller.
	// using the length returned by your function, it prints the first len elements.
	for (int i = 0; i < len; i++) 
	{
    	//printf("%d ",nums[i]);
	}
	return 0;
}