## longest-harmonious-subsequence

```java
Subsequence: A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Input: int[] nums
先Arrays.sort(nums)， 保持数组顺序，方便后面计算
时间： O(n*log(n)) -> Quick Sort 
空间： O(n)
https://leetcode.cn/problems/longest-harmonious-subsequence/
```

### Quick Sort 快速排序
采用分治的思想，先找到 每次分割的点 pos 
```java
/*
    left:数组左边界
    right：数组右边界
    */
    public void quickSort(int[] arr, int left, int right){
        if(left < right){
            int pos = partition(arr, left, right);
            quickSort(arr, left, pos - 1);
            quickSort(arr, pos + 1, right);
        }
    }
    public int partition(int[] arr, int left, int right){
        int base = arr[left]; // 暂时的place holder
        while(left < right){
            while(left < right && arr[right] >= base){
                right--;
            }
            // 找到一个 <= base 的数字, 
            arr[left] = arr[right];
            while(left < right && arr[left] <= base){
                left++;
            }
            arr[right] = arr[left];       
        }
        arr[left] = base;
        return left;
    }


```
