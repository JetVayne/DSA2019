###### tags: `GitHub - DSA2019`
# What is Queue ?
> <font size = 2 >Original Author : [aaron1aaron2](https://github.com/aaron1aaron2) -《[Stack & Queue](https://github.com/aaron1aaron2/my-learning-note/tree/master/week3)》</font>

<br>

![](https://i.imgur.com/FRWYs3b.png)
<br><br>

## 為什麼要有 Queue
* **應用在其他演算法**: 
    * Bread-First Search | 廣度優先搜尋
    * Tree 的 Level-Order Traversal | 二元樹走訪
* 作業係統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。

## Queue 的功能
* **Push(Data)**: 把資料放到 Queue 的後面，並更新成新的 back。
* **Pop(dequeue)**: 把 front 所指向的資料從 Queue 中移除，並更新front。
* **getFront**: 回傳 front 所指向的資資料。
* **getBack**: 回傳 Back 所指向的資資料。
* **IsEmpty**: 確認 Queue 裡是否有資料。
* **getSize**: 確認 Queue 裡的資料個數。


