### 问题描述：
***
    给定有符号整数，输出该整数的按位取反数（例如：给-123,返回-321），注意整数取值范围。
***

```c
#define MAXINT pow(2,31)-1
#define MININT -pow(2,31)

int reverse(int x) 
{
	long reverX = 0;//反转数
	int n = 0;//分配n 个int型临时内存
	long num_one;
	int* pt;
	bool flag = true;//正负标识
		if (x < 0)
		{
			flag = false;
		}
		num_one  = abs(x);
		//计算位数
		while (num_one != 0)
		{
			n++;
			num_one /= 10;
		}
		num_one = abs(x);
		//分配临时内存并初始化为0
		pt = (int*)calloc(n , sizeof(int));

		for (int i = 0; i < n; i++)
		{
			*(pt+i) = num_one % 10;
			num_one /= 10;
		}
		for (int i = 0; i < n; i++) 
		{
			reverX += *(pt + i) * pow(10, n-i-1);
		}
		if (!flag)
		{
			reverX = -reverX;
		}
	
	free(pt);
	if (reverX > MAXINT || reverX < MININT)//超出范围，返回0
	{
		return 0;
	}
	else
	{
		return reverX;
	}
}
```