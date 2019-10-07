class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head: ListNode) -> ListNode:
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        self.sort_list(node_list)

        # curr = new_node = ListNode(0)
        result_node = ListNode(0)
        curr_node = result_node

        for data in node_list:
            curr_node.next = ListNode(data)
            curr_node = curr_node.next

        return result_node.next

    def sort_list(self, input_list: list):
        for curr_index in range(1, len(input_list)):
            check_value = input_list[curr_index]
            prev_index = curr_index - 1
            while prev_index >= 0:
                if check_value < input_list[prev_index]:
                    input_list[prev_index + 1] = input_list[prev_index]
                    input_list[prev_index] = check_value
                    prev_index -= 1
                else:
                    break

