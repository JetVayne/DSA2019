# coding: utf-8

import os


def merge(array: int, start: int, mid: int, end: int):
    print('做merge')
    print()
    target_len = end - start + 1
    left_list = []
    right_list = []
    result = []

    for i in range(start, mid + 1):
        left_list.append(array[i])

    for i in range(mid + 1, end + 1):
        right_list.append(array[i])


    while len(result) != target_len:
        if len(right_list) == 0 and len(left_list) != 0:
            result.append(left_list.pop(0))
            continue
        if len(left_list) == 0 and len(right_list) != 0:
            result.append(right_list.pop(0))
            continue
        if len(left_list) != 0 and len(right_list) != 0:
            if left_list[0] <= right_list[0]:
                result.append(left_list.pop(0))
            else:
                result.append(right_list.pop(0))

    # print(result)
    for i in range(start,end+1):
        array[i] = result.pop(0)



def sorter_left(array: list, start_index: int, end_index: int, big_mid: int):
    curr_mid = (start_index + end_index) // 2
    # print('@@@@@@@@@@')
    # print('@中間:', curr_mid)
    # print('@左:', start_index, '@右:', end_index)

    if start_index < end_index:
        # print('@中間:', curr_mid)
        # print('@左:', start_index, '@右:', end_index)
        sorter_left(array, start_index, curr_mid, big_mid)
        sorter_left(array,curr_mid + 1, end_index,big_mid)
        # print('做比較 - 中間:', curr_mid, '左:', start_index, '右:', end_index)
        if curr_mid != big_mid:
            print('------------------')
            print('中間:', curr_mid)
            print('左:', start_index, '右:', end_index)
            merge(array, start_index, curr_mid, end_index)
            # return
        else:
            print('$$$')

        # merge(array, start_index, middle, end_index)
    else:
        print('開始:',start_index,'結束:',end_index)
        print('**** 跳出')


def merge_sort(array: list):
    total_len = len(array)

    big_mid = (len(array) - 1) // 2

    # sort左邊
    sorter_left(array, 0, len(array) - 1, big_mid)


a = [7, 4, 8, 5, 6, 5, 3]
# a = [4, 7, 8, 5, 6, 5, 3, 4, 7, 8, 5, 6, 5, 3, 4, 7, 8, 5, 6, 5, 3]
merge_sort(a)
print(a)

