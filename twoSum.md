### 问题描述：
> 给定整数数组及特定整数a,从数组元素中找出两个数b、c，若b+c=a,返回元素b、c下标
```c

#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target) {
    int i,j;
    int count = 0;
    
    int* ptd = (int *)malloc(2*sizeof(int));//分配动态内存
    if(ptd == NULL)//内存空间分配出错，退出
    {
        exit(EXIT_FAILURE);
    }
    //循环判断
    for(i = 0;i < numsSize-1; i++)
    {
        for(j = i+1;j < numsSize; j++)
        {
            if(*(nums+i) + *(nums+j) == target)
            {
               *(ptd+count++) = i;
                *(ptd+count) = j;
               i = numsSize;
                break;
            }
        }
    }
     //free(ptd);
    return ptd;
}
```

