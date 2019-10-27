# coding: utf-8

'''
author: Jet Vayne
'''


def get_partition(sequence, left_index, right_index, pivot):
    while left_index <= right_index:
        '''
        左邊理論上要比 pivot 小， 所以 while 設 array[left] < pivot
        依序向右邊增加 index 和 pivot 做比較
        '''
        while sequence[left_index] < pivot:
            left_index += 1

        '''
        右邊理論上要比 pivot 大， 所以 while 設 array[right] > pivot
        依序向左邊遞減 index 和 pivot 做比較
        '''
        while sequence[right_index] > pivot:
            right_index -= 1

        # 做換位動作
        if left_index <= right_index:
            temp = sequence[left_index]
            sequence[left_index] = sequence[right_index]
            sequence[right_index] = temp
            left_index += 1
            right_index -= 1


    return left_index


def sorter(sequence, left_index, right_index):
    if left_index >= right_index:
        return

    # 隨機取 pivot
    median_index = (left_index + right_index) // 2  # // 兩槓去小數
    pivot = sequence[median_index]

    # 找到截斷點，之後要分左右段
    partition = get_partition(sequence, left_index, right_index, pivot)
    # print(partition, sequence[partition], pivot)

    # 左段
    sorter(sequence, left_index, partition - 1)

    # 右段
    sorter(sequence, partition, right_index)


#   可以自由設定頭尾 index 參數, 若只 input 集合，預設為從頭到尾
def quick_sort(sequence: list, start_index=None, end_index=None):
    # default
    if start_index is None and end_index is None:
        start_index = 0
        end_index = len(sequence) - 1
    # 只設定頭
    elif start_index and end_index is None:
        end_index = len(sequence) - 1
    # 只設定尾
    elif end_index and start_index is None:
        start_index = 0

    sorter(sequence, start_index, end_index)


input_list = [3, 8, 9, 11, 25, 2, 1, 11, -2, 10, -2, 5, 6, -8]

print('before:', input_list)
print()
quick_sort(input_list)
print('after:', input_list)
