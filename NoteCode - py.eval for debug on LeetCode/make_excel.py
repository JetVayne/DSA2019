import pandas as pd

function = ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtTail", "get", "addAtIndex", "addAtHead", "addAtHead",
            "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "addAtIndex", "get", "get", "addAtIndex", "get",
            "addAtHead", "addAtIndex", "addAtIndex", "addAtHead", "addAtIndex", "addAtIndex", "addAtHead", "get",
            "deleteAtIndex", "addAtIndex", "get", "get", "deleteAtIndex", "addAtTail", "addAtHead", "addAtTail",
            "addAtHead", "addAtTail", "addAtTail", "addAtIndex", "get", "get", "addAtHead", "deleteAtIndex",
            "deleteAtIndex", "get", "deleteAtIndex", "get", "addAtIndex", "addAtTail", "addAtHead", "addAtTail",
            "addAtHead", "get", "addAtTail", "addAtTail", "addAtHead", "get", "get", "addAtHead", "addAtHead",
            "addAtIndex", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtTail", "addAtIndex",
            "addAtHead", "addAtTail", "deleteAtIndex", "addAtHead", "addAtHead", "addAtIndex", "addAtTail",
            "addAtIndex", "addAtTail", "addAtIndex", "get", "addAtIndex", "addAtIndex", "get", "addAtTail", "addAtTail",
            "addAtHead", "addAtHead", "addAtHead", "deleteAtIndex", "addAtHead", "addAtTail", "addAtTail", "addAtTail",
            "addAtTail", "addAtHead", "addAtHead", "addAtTail", "addAtTail", "addAtIndex", "get", "addAtTail",
            "addAtHead", "addAtTail", "addAtHead"]

input = [[], [56], [1], [41], [98], [3], [1, 33], [72], [52], [89], [0], [98], [7, 97], [2, 51], [1], [6], [6, 49], [8],
         [72], [7, 8], [8, 58], [10], [3, 6], [9, 61], [63], [16], [7], [16, 55], [4], [10], [6], [96], [69], [20], [3],
         [44], [4], [8, 16], [15], [21], [41], [1], [11], [21], [22], [2], [5, 7], [62], [95], [91], [69], [24], [51],
         [94], [93], [29], [10], [68], [13], [32, 42], [48], [55], [79], [5], [36], [32], [25, 40], [8], [68], [30],
         [66], [92], [27, 26], [90], [11, 19], [68], [17, 62], [15], [17, 97], [35, 89], [44], [90], [67], [2], [51],
         [30], [38], [30], [43], [76], [16], [38], [82], [81], [67], [67], [3, 16], [57], [94], [11], [31], [50]]

output = ['null', 'null', -1, 'null', 'null', -1, 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 0, 41,
          'null', 33, 'null', 'null', 'null', 'null', 'null', 'null', 'null', 97, 'null', 'null', 6, 8, 'null', 'null',
          'null', 'null', 'null', 'null', 'null', 'null', 41, 96, 'null', 'null', 'null', 20, 'null', 63, 'null',
          'null', 'null', 'null', 'null', 44, 'null', 'null', 'null', 51, 6, 'null', 'null', 'null', 'null', 'null',
          'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null',
          'null', 'null', 69, 'null', 'null', 51, 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null',
          'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 90, 'null', 'null', 'null', 'null']

exp = ['null', 'null', -1, 'null', 'null', -1, 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 0, 41,
       'null', 33, 'null', 'null', 'null', 'null', 'null', 'null', 'null', 97, 'null', 'null', 6, 8, 'null', 'null',
       'null', 'null', 'null', 'null', 'null', 'null', 41, 96, 'null', 'null', 'null', 20, 'null', 63, 'null', 'null',
       'null', 'null', 'null', 20, 'null', 'null', 'null', 51, 6, 'null', 'null', 'null', 'null', 'null', 'null',
       'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null',
       69, 'null', 'null', 51, 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null', 'null',
       'null', 'null', 'null', 'null', 'null', 90, 'null', 'null', 'null', 'null']

df = pd.DataFrame({'Fuction': function, 'Input': input, 'Output': output, 'Expected': exp})
df['Check'] = df['Output'] == df['Expected']
df.to_excel(excel_writer = "D:/debug.xlsx",index=False)
