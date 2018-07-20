### 问题描述：
***
给定整数，若反转后与原整数相等，返回true否则返回false
### 代码实现
***
```c
bool isPalindrome(int x) {
    int m = 0;
    int n = x;
    
    if(x < 0) {
        return false;
    }else if(x < 10){
        return true;
    }else{
        while(x){
            m = m*10+x%10;
            x /= 10;
        }
        if(n == m){
            return true;
        }
        return false;
    }
}
```