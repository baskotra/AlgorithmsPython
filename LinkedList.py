class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "->"
                current_node = current_node.get_next_node()
        string_list += "None"
        return string_list

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_last(self, value):
        new_node = Node(value)
        current_node = self.head_node
        while current_node:
            if current_node.get_next_node() is None:
                current_node.set_next_node(new_node)
                break
            current_node = current_node.get_next_node()

    def reverse(self):
        prev = None
        current = self.head_node
        while(current is not None):
            next_node = current.get_next_node()
            current.set_next_node(prev)
            prev = current
            current = next_node
        self.head_node = prev

    def middle_element(self):
        slow_ptr = self.head_node
        fast_ptr = self.head_node

        if self.head_node is not None:
            while (fast_ptr is not None and fast_ptr.get_next_node() is not None):
                fast_ptr = fast_ptr.get_next_node().get_next_node()
                slow_ptr = slow_ptr.get_next_node()
            return slow_ptr.get_value()


ll = LinkedList(2)
ll.insert_beginning(1)
ll.insert_last(3)
ll.insert_last(4)
# print(ll.stringify_list())
# ll.reverse()
# print(ll.stringify_list())
print(ll.middle_element())
