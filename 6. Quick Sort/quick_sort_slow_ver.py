def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    bigger_list = []
    smaller_list = []

    for item in sequence:
        if item > pivot:
            bigger_list.append(item)
        else:
            smaller_list.append(item)

    return quick_sort(smaller_list) + [pivot] + quick_sort(bigger_list)


list = [3, 8, 9, 11, 25, 2, 1, 11, -2, 10, -2, 5, 6, -8]
print('before:', list)
result = quick_sort(list)
print('result:', result)
