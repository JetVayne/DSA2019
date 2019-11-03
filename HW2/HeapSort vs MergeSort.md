###### tags: `GitHub - DSA2019`
# Heap Sort vs Merge Sort
### 兩者在效能上，在 best case、average case、worst case 的情況下，時間複雜度都是 n log n
### 而兩者最大的差別在於「排列的方式」

## Heap Sort 的排列方式
透過將 list 內所有的元素依照 max heap 或是 min heap 的資料結構去排列，使該 list 變成一個 "heap"，再將 root 取出後，重新讓 list 內剩餘的元素重新排列，並且符合 heap 的資料結構，而後再取出root，不斷的重複取 root 以及 heapify 的動作，直到 sorting 完成

## Merge Sort 的排列方式
Merge Sort 有點像是堆金字塔的感覺，先將小東西都排序完後再合併，變成大一點的東西之後再繼續跟同等級的東西排序。Merge Sort 會先將所有的元素都視為 sub-list，再彼此排序合併，level 提升後再繼續找跟自己同 level 的 sub-list 做比值排序並合併，不停地重複這些動作，直到完成最高 level 的 merge。
