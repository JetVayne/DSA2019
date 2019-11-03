###### tags: `GitHub - DSA2019`
# Merge Sort
## Reference
[![Merge Sort Tutorial Video](https://i1.ytimg.com/vi/mB5HXBb_HY8/hqdefault.jpg)](https://www.youtube.com/watch?v=mB5HXBb_HY8)
<br>
這部影片中沒有任何的程式碼，只有關於 Merge Sort 的概念、邏輯解說。非常感謝 Abdul Bari 精美的板書，Merge Sort 的板書解說其實非常簡單，也很好理解，不過實際用程式邏輯去操作我個人認為超他媽難，
後半段 Abdul Bari 的解說我覺得也沒有解釋得非常好讓人理解。

## Diagram
![](https://i.imgur.com/d6c8vPj.jpg)

## Reflection
從看影片、完全吸收影片知識到完美的用程式把 Merge Sort 實做出來，大概花了8個小時，和 Heap Sort 相比，多花了整整3小時。
<br>

在順利的完成 Heap Sort 後，成就感與自信有得到提升，所以 Merge Sort 當然也會挑戰在不看任何程式碼的情況下，從0到100，試著去完成它。
<br>

不過我覺得 Merge Sort 非常奇怪，明明邏輯規則非常淺顯易懂，但就是很難用程式去實現它，主要是我一開始不太知道怎麼用 recursive 把所有 sub-list 切出來，其實一開始有想到先一直遞迴到最後，遞迴完畢後再做 merge，但是我非常排斥這樣寫，因為我覺得遞迴就應該在那一次 re-call 之前把事情都做完才 re-call，覺得如果不這樣做，好像會發生問題，但是我想破頭，我還是想不到更好的辦法。最後確定先遞迴再 merge 好像沒有問題，我才確實地把 merger sort 寫完，之後可能會再看看網上有那些高手有什麼漂亮的做法吧?
<br>

感覺 Merge Sort 最難的是把 sub-list 的部分切出來，所以我覺得 sorter 的部分最難寫，而 merge 這個動作基本上我認為是非常好寫的。
