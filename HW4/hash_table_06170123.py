from Crypto.Hash import MD5


class ListNode(object):
    def __init__(self, val: str):
        self.val = val
        self.next = None


class MyHashSet(object):
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key: str):
        key_code = self.get_key_code(key)
        save_index = key_code % self.capacity

        if self.data[save_index] is None:
            self.data[save_index] = ListNode(key)
        else:
            curr_node = self.data[save_index]
            if not self.already_saved(curr_node, key):
                flag = True
                while flag:
                    if curr_node.next is None:
                        curr_node.next = ListNode(key)
                        flag = False
                    else:
                        curr_node = curr_node.next
            else:
                print('already saved !')

    def get_key_code(self, key: str):
        if key is None:
            return key
        result = MD5.new()
        result.update(key.encode('utf-8'))
        result = int(result.hexdigest(), 16)

        return result

    def already_saved(self, node: ListNode, key: str):
        result = False
        curr_node = node
        while curr_node:
            if curr_node.val == key:
                return True
            curr_node = curr_node.next

        return result

    def remove(self, key: str):
        key_code = self.get_key_code(key)
        del_index = key_code % self.capacity
        if self.data[del_index] is None:
            print('can not remove !')
            return
        else:
            curr_node = self.data[del_index]
            if self.already_saved(curr_node, key):
                # the head is del target
                if curr_node.val == key:
                    self.data[del_index] = curr_node.next

                else:
                    flag = True
                    while flag:
                        if curr_node.next.val == key:
                            curr_node.next = curr_node.next.next
                            flag = False
            else:
                print('can not remove !')

    def contains(self, key: str) -> bool:
        key_code = self.get_key_code(key)
        exist_index = key_code % self.capacity
        if self.data[exist_index] is None:
            return False
        else:
            curr_node = self.data[exist_index]
            if self.already_saved(curr_node, key):
                return True
            else:
                return False

