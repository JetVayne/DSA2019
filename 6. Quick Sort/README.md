###### tags: `GitHub - DSA2019`
# Version 1 - 多 List append 方法

使用 recursiven 方法。
<br>
處理資料次數 X 與 recursive 次數 n 的關係:
<br>
![](https://i.imgur.com/VHFKWBl.png)
<br><br>
![](https://i.imgur.com/BlppxgP.jpg)
<br>

此方法雖然看似非常乾淨簡單，但是效能似乎沒有真的達到 O(n log n)，因為我在寫 [LeetCode - 148. Sort List](https://leetcode.com/problems/sort-list/) 的時候，發現直接使用這種方法，去排序ListNode，submit 後會因為效能沒有達到O(n log n)而失敗。有可能是因為指派過多 List 的關係。
<br><br>

![](https://i.imgur.com/jBvf460.png)

<br><br>
在看過其他人的做法後發現，再加上 partition 後比對，能不用全部 itter 集合再 append 值，能利用 partition 查看 index 的值，再做換位，省去 itter 的動作

# Version 2 - 單一 List 換位法
<br><br>

![](https://i.imgur.com/AL7MqF4.jpg)

<br><br>

再將新程式碼套用在 [LeetCode - 148. Sort List](https://leetcode.com/problems/sort-list/) 中 sort ListNode 的部分。

<br><br>

![](https://i.imgur.com/eIoezBu.png)

<br><br>

成功 submit !


