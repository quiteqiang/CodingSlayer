## Two - Sum
```java
// 使用Map 让数字不重复统计
// - 重点： Map 的操作
Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < nums.length; i++){
    if (map.containsKey(target-nums[i])){
      return new int[] {i, map.get(target-nums[i])};
    }
    map.put(nums[i], i);
}
return new int[]{};
```