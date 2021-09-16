from time import sleep


class Node:
    def __init__(self, data):
        self.head = data
        self.next = None
        self.previous = None

    def __repr__(self):
        self.data = self.head
        return self.data


class Linkedlist:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with data {target_node_data} not found')

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')
        sleep(1)
        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found ')

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node =node

        raise Exception(f'Node with data {target_node_data} not found')


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point= None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes =[]
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print('->'.join(nodes))
if __name__ == '__main__':
    llist = Linkedlist()
    first_node = Node('a')
    llist.head = first_node
    second_node = Node('b')
    third_node = Node('c')
    first_node.next = second_node
    second_node.next = third_node
    print()

#Example: print node
    llist = Linkedlist(['a', 'b', 'c', 'd', 'e'])
    print()
    for node in llist:
        print(node)

#Example: add_first method
    llist = Linkedlist()
    llist.add_first(Node('b'))
    llist.add_first(Node('a'))

#Example: add_last method
    llist = Linkedlist(['a', 'b', 'c', 'd'])
    llist.add_last(Node('e'))
    llist.add_last(Node('f'))

#Example: add_after method
    llist = Linkedlist()
    try:
        llist.add_after('a', Node('b'))
    except:
        print(f'Error')
    llist = Linkedlist(['a', 'b', 'c', 'd'])
    try:
        llist.add_after('c', Node('cc'))
        llist.add_after('f', Node('g'))
    except:
        print(f'Error')

#Example: add_before method
    llist = Linkedlist(['b', 'c'])
    try:
        llist.add_before('b', Node('a'))
        llist.add_before('b', Node('aa'))
        llist.add_before('c', Node('bb'))
    except:
        pass
    try:
        llist.add_before('n', Node('m'))
    except:
        print(f'Error')

#Example: remove_node method
    llist = Linkedlist()
    try:
        llist.remove_node('a')
    except:
        print(f'Error')
    llist = Linkedlist(['a', 'b', 'c', 'd', 'e'])
    try:
        llist.remove_node('a')
        llist.remove_node('e')
        llist.remove_node('c')
    except:
        pass
    try:
        llist.remove_node('a')
    except:
        print(f'Error')

#Example:
    circular_list = CircularLinkedList()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    circular_list.head = a
    circular_list.print_list()
    circular_list.print_list(b)
    circular_list.print_list(d)